#!/usr/bin/env bash
set -euo pipefail

package_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
source_dir="$package_dir/../plugins/design-router/skills/design-router"
target_kind="codex"
dry_run="false"

usage() {
  printf '%s\n' \
    'Usage: ./install.sh [--target codex|agents|PATH] [--dry-run]' \
    '' \
    'Copies this local design-router skill only. No network access or third-party installs.'
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --target)
      [ "$#" -ge 2 ] || { usage; exit 2; }
      target_kind="$2"
      shift 2
      ;;
    --dry-run)
      dry_run="true"
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      printf 'Unknown argument: %s\n' "$1" >&2
      usage >&2
      exit 2
      ;;
  esac
done

case "$target_kind" in
  codex)
    target_root="${CODEX_HOME:-$HOME/.codex}/skills"
    ;;
  agents)
    target_root="${AGENTS_HOME:-$HOME/.agents}/skills"
    ;;
  *)
    target_root="$target_kind"
    ;;
esac

destination="$target_root/design-router"
timestamp="$(date '+%Y%m%d-%H%M%S')"
backup="$target_root/design-router.backup-$timestamp"

printf 'Source:      %s\n' "$source_dir"
printf 'Destination: %s\n' "$destination"

if [ "$dry_run" = "true" ]; then
  if [ -e "$destination" ]; then
    printf 'Existing destination would be backed up to: %s\n' "$backup"
  fi
  printf '%s\n' 'Dry run complete. No files changed.'
  exit 0
fi

mkdir -p "$target_root"
if [ -e "$destination" ]; then
  mv "$destination" "$backup"
  printf 'Backed up existing router to: %s\n' "$backup"
fi

cp -R "$source_dir" "$destination"
printf 'Installed design-router at: %s\n' "$destination"
printf '%s\n' 'Restart Codex so the new skill is discovered.'
