#!/usr/bin/env python3
"""Read-only, explicit-scope skill inventory. Python 3.11+, standard library only."""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
import os
from pathlib import Path
import re
import tomllib

SKIP = {'.git', 'node_modules', '__pycache__', '.venv'}
MAX_FILE_BYTES = 2_000_000
MAX_BUNDLE_BYTES = 20_000_000


def digest(data):
    return hashlib.sha256(data).hexdigest()


def walk_skills(root, warnings, ancestors=frozenset()):
    """Follow aliases but stop cycles; a skill's resources are not new skill roots."""
    try:
        real = root.resolve(strict=True)
        if real in ancestors:
            warnings.append(f'Symlink cycle skipped: {root}')
            return
        if not root.is_dir():
            warnings.append(f'Not a directory: {root}')
            return
        if (root / 'SKILL.md').is_file():
            yield root / 'SKILL.md'
            return
        for child in sorted(root.iterdir()):
            if child.name not in SKIP and child.is_dir():
                yield from walk_skills(child, warnings, ancestors | {real})
    except (OSError, RuntimeError) as exc:
        warnings.append(f'Unreadable root {root}: {type(exc).__name__}')


def bundle_fingerprint(root):
    """Include resources; mark skipped/linked/large material as incomplete, not equal."""
    entries, limits = [], []
    total = 0
    pending = [root]
    while pending:
        folder = pending.pop()
        try:
            children = sorted(folder.iterdir())
        except OSError:
            limits.append(f'unreadable directory: {folder.relative_to(root)}')
            continue
        for p in children:
            rel = p.relative_to(root).as_posix()
            try:
                if p.name in SKIP or p.name.startswith('.env'):
                    limits.append(f'excluded: {rel}')
                elif p.is_symlink():
                    limits.append(f'linked resource: {rel}')
                elif p.is_dir():
                    pending.append(p)
                elif p.is_file():
                    size = p.stat().st_size
                    if size > MAX_FILE_BYTES or total + size > MAX_BUNDLE_BYTES:
                        limits.append(f'size limit: {rel}')
                        continue
                    data = p.read_bytes()
                    total += len(data)
                    entries.append((rel, digest(data)))
            except OSError:
                limits.append(f'unreadable resource: {rel}')
    return (digest(json.dumps(sorted(entries)).encode()) if not limits else None), limits


def metadata(text, key):
    """Extract common scalar frontmatter without interpreting YAML or executing it."""
    text = text.replace('\r\n', '\n')
    if not text.startswith('---\n'):
        return None
    front = text.split('---', 2)[1]
    match = re.search(r'^' + re.escape(key) + r':[ \t]*(.+)$', front, re.M)
    if not match or match[1].strip() in {'>', '|', '>-', '|-'}:
        return None
    return match[1].strip().strip('\"\'')


def plugin_roots(snapshot, codex_home, warnings):
    roots = []
    for plugin in snapshot.get('installed', []):
        if plugin.get('installed') is not True:
            continue
        ident = plugin.get('pluginId', '')
        name, separator, market = ident.rpartition('@')
        version = plugin.get('version')
        if not separator or not version or any('/' in str(x) or '\\' in str(x) or str(x) in {'.', '..'} for x in (name, market, version)):
            warnings.append(f'Cannot resolve exact plugin version: {ident}')
            continue
        package = codex_home / 'plugins/cache' / market / name / str(version)
        material = 'exact-version-cache'
        if not package.is_dir():
            source = plugin.get('source', {})
            source_path = source.get('path') if source.get('source') == 'local' else None
            if not source_path or not Path(source_path).is_dir():
                warnings.append(f'No local material for listed version: {ident} {version}')
                continue
            package = Path(source_path)
            material = 'declared-source-not-loaded-cache'
        manifest_path = package / '.codex-plugin/plugin.json'
        manifest = {}
        if manifest_path.exists():
            try:
                manifest = json.loads(manifest_path.read_text())
            except (OSError, ValueError):
                warnings.append(f'Unreadable plugin manifest: {ident}')
                continue
        if manifest.get('version') and str(manifest['version']) != str(version):
            warnings.append(f'Manifest/listed version mismatch: {ident}')
            continue
        paths = manifest.get('skills', './skills')
        paths = [paths] if isinstance(paths, str) else paths
        if not isinstance(paths, list) or not all(isinstance(x, str) for x in paths):
            warnings.append(f'Unsupported skills manifest: {ident}')
            continue
        migrated = '.codex-plugin/migrated-command-skills'
        if (package / migrated).is_dir() and migrated not in paths:
            paths.append(migrated)
        for rel in paths:
            root = package / rel
            if not root.resolve().is_relative_to(package.resolve()):
                warnings.append(f'External plugin skill root needs inspection: {ident} {rel}')
                continue
            if root.is_dir():
                roots.append({'label': ident, 'path': str(root), 'plugin_id': ident,
                              'plugin_name': name, 'plugin_enabled': plugin.get('enabled'),
                              'version': version, 'materialization': material,
                              'package_contributions_verified': False})
            elif 'skills' in manifest:
                warnings.append(f'Declared skill root missing: {ident} {rel}')
    return roots


def inventory(roots, disabled=(), warnings=None):
    warnings = [] if warnings is None else warnings
    records, seen, fingerprints = [], set(), {}
    for root in roots:
        for p in walk_skills(Path(root['path']).expanduser().absolute(), warnings):
            identity = (root['label'], str(p))
            if identity in seen:
                continue
            seen.add(identity)
            try:
                if p.stat().st_size > MAX_FILE_BYTES:
                    warnings.append(f'Skill entrypoint exceeds size limit: {p}')
                    continue
                data = p.read_bytes()
                text = data.decode('utf-8-sig')
                real = p.resolve()
                name = metadata(text, 'name')
                if not name:
                    warnings.append(f'Unparsed skill name, using folder: {p}')
                    name = p.parent.name
                if real not in fingerprints:
                    fingerprints[real] = bundle_fingerprint(real.parent)
                bundle, limits = fingerprints[real]
                matches = []
                for rule in disabled:
                    if rule.get('enabled') is not False:
                        continue
                    rulepath = rule.get('path')
                    names = {name, f"{root.get('plugin_name')}:{name}"} if root.get('plugin_name') else {name}
                    if (rulepath and Path(rulepath).expanduser().resolve() == real) or rule.get('name') in names:
                        matches.append({k: rule[k] for k in ('path', 'name') if k in rule})
                excluded = root.get('plugin_enabled') is False or bool(matches)
                records.append({**root, 'id': len(records), 'path': str(p),
                                'real_path': str(real), 'name': name,
                                'description': metadata(text, 'description'),
                                'entrypoint_sha256': digest(data), 'bundle_sha256': bundle,
                                'fingerprint_limits': limits,
                                'matching_disable_rules': matches,
                                'activity': 'disabled-in-inventory' if excluded else 'candidate-not-session-verified'})
            except (OSError, UnicodeError, RuntimeError) as exc:
                warnings.append(f'Unreadable skill {p}: {type(exc).__name__}')
    groups = []
    for kind, field in [('path-alias', 'real_path'), ('same-local-bundle', 'bundle_sha256'),
                        ('same-entrypoint', 'entrypoint_sha256'), ('same-name', 'name')]:
        buckets = defaultdict(list)
        for r in records:
            if r[field]:
                buckets[r[field]].append(r)
        for key, members in sorted(buckets.items()):
            if len(members) < 2:
                continue
            if kind != 'path-alias' and len({r['real_path'] for r in members}) < 2:
                continue
            groups.append({'kind': kind, 'key': key, 'members': [r['id'] for r in members],
                           'potentially_active_members': sum(r['activity'] != 'disabled-in-inventory' for r in members)})
    return {'schema_version': 1, 'read_only': True, 'roots': roots, 'skills': records,
            'groups': groups, 'warnings': warnings,
            'limits': ['Filesystem and supplied state only; session visibility is unverified.',
                       'Fingerprint equality covers local files only, not external references, plugin tools or hooks.',
                       'Name/entrypoint matches are candidates, not a cleanup decision.',
                       'Only supplied config is read; project, profile and managed precedence is not resolved.',
                       'Disable-rule matches require host targeting and config-precedence verification.']}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', action='append', default=[], metavar='LABEL=PATH')
    parser.add_argument('--plugin-list', type=Path)
    parser.add_argument('--codex-home', type=Path)
    parser.add_argument('--config', type=Path)
    parser.add_argument('--output', type=Path, help='New report file; refuses to overwrite')
    args = parser.parse_args()
    roots, warnings = [], []
    for item in args.root:
        label, sep, path = item.partition('=')
        if not sep or not label or not path:
            parser.error('--root must be LABEL=PATH')
        roots.append({'label': label, 'path': path, 'materialization': 'explicit-root'})
    try:
        if args.plugin_list:
            if not args.codex_home:
                parser.error('--plugin-list requires --codex-home')
            snapshot = json.loads(args.plugin_list.read_text())
            if not isinstance(snapshot.get('installed'), list):
                parser.error('plugin inventory must contain an installed array')
            roots.extend(plugin_roots(snapshot, args.codex_home.expanduser(), warnings))
        disabled = []
        if args.config:
            disabled = tomllib.loads(args.config.read_text()).get('skills', {}).get('config', [])
        if not roots:
            parser.error('provide at least one root or resolvable installed plugin')
        report = inventory(roots, disabled, warnings)
        report['config_source'] = str(args.config) if args.config else None
        report['config_precedence_resolved'] = False
        rendered = json.dumps(report, indent=2) + '\n'
        if args.output:
            # Exclusive creation also prevents following an existing output symlink.
            fd = os.open(args.output, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
            with os.fdopen(fd, 'w') as stream:
                stream.write(rendered)
            print(json.dumps({'skills': len(report['skills']), 'candidate_groups': len(report['groups']),
                              'warnings': len(report['warnings']), 'report': str(args.output)}))
        else:
            print(rendered, end='')
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(1, f'Inventory failed: {type(exc).__name__}: {exc}\n')


if __name__ == '__main__':
    main()
