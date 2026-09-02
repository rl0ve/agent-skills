#!/usr/bin/env python3
"""Flag high-signal writing patterns for human review; never infer authorship.

Three rules -- contrastive-definition, deferred-point and mechanism-speak -- are
frequency findings. A single hit is ordinary prose. Treat them as a problem when
they recur across a piece, or across a set being edited to one standard, and read
the catalog's "Editing a set" before acting on them.

Two whole-piece checks live outside scan(): em-dash-overuse (density, not a
single instance), sentence-shape-run (four or more consecutive sentences in one
paragraph sharing the same compound/hedged-or-simple shape), flat-declarative-run
(three or more consecutive sentences of near-identical length that none of them
turns) and stacked-precision (three or more consecutive sentences each landing an
exact figure).
"""

from __future__ import annotations

import argparse
import math
import json
import re
from collections import Counter
from pathlib import Path


PATTERNS = {
    "throat-clearing": re.compile(
        r"\b(?:here(?:'s| is) the thing|it(?:'s| is) worth noting|in today(?:'s|’s) world|let(?:'s| us) dive in)\b",
        re.IGNORECASE,
    ),
    "importance-inflation": re.compile(
        r"\b(?:pivotal moment|transformative milestone|plays? a vital role|stands? as a testament|underscores? (?:its|the) significance)\b",
        re.IGNORECASE,
    ),
    "vague-attribution": re.compile(
        r"\b(?:experts (?:say|agree|argue)|studies show|industry reports suggest|many observers believe)\b",
        re.IGNORECASE,
    ),
    "nominated-significance": re.compile(
        r"\b(?:is|are) the point\b|\bthat is the point\b|\bwhich is the point\b|\bthe point is\b"
        r"|\bis what matters\b|\bwhat matters is\b|\bthe thing to notice\b"
        r"|\bthe real (?:story|question|answer) is\b|\bis the interesting (?:bit|part|thing)\b",
        re.IGNORECASE,
    ),
    "backwards-facing-clause": re.compile(
        r"\b(?:(?:built|designed|made|meant) for (?:exactly )?that\b"
        r"|exactly that\b"
        r"|the way (?:it|they|he|she|the \w+) (?:said|described|promised)\b"
        r"|where nothing (?:\w+ )?them\b"
        r"|which is what (?:it|they|this|that) (?:does|did|means?)\b)",
        re.IGNORECASE,
    ),
    "binary-template": re.compile(
        r"\b(?:it(?:'s| is) not (?:just|only)|not only\b.{0,80}\bbut also|the (?:question|issue) (?:isn't|is not)\b.{0,80}\bit(?:'s| is))",
        re.IGNORECASE,
    ),
    "superficial-analysis": re.compile(
        r",\s+(?:highlighting|underscoring|showcasing|reflecting|demonstrating)\b",
        re.IGNORECASE,
    ),
    "stock-ai-vocabulary": re.compile(
        r"\b(?:delve|ever-evolving|tapestry|multifaceted|paramount|supercharge|game[- ]changer)\b",
        re.IGNORECASE,
    ),
    "chatbot-residue": re.compile(
        r"\b(?:i hope this helps|feel free to ask|let me know if you(?:'d| would) like|happy to help)\b",
        re.IGNORECASE,
    ),
    "validation-preamble": re.compile(
        r"^\s*(?:great question|you(?:'re| are) absolutely right|that(?:'s| is) exactly right|you(?:'ve| have) put your finger on)\b",
        re.IGNORECASE,
    ),
    "collaboration-theater": re.compile(
        r"\b(?:one thing i want to push on gently|may be hard to see from inside|you probably can(?:'t| not) see from inside)\b",
        re.IGNORECASE,
    ),
    "question-answer-pivot": re.compile(
        r"\b(?:the result|the catch|the problem|the payoff|what changed)\?\s+(?:a|an|the|it|everything|nothing)\b",
        re.IGNORECASE,
    ),
    "dash-cluster": re.compile(r"(?:—|–|\s--\s)"),
    "contrastive-definition": re.compile(
        r"\b(?:rather than|instead of)\b",
        re.IGNORECASE,
    ),
    "deferred-point": re.compile(
        r",\s+(?:so|which is what|which keeps|which stops|which makes)\b",
        re.IGNORECASE,
    ),
    # A finished sentence, then two or more verbless attribute phrases closing
    # the line. "Plain language, no jargon, ready to use as it stands."
    "spec-sheet-coda": re.compile(
        r"(?<=[.!?])\s+(?!(?:[A-Z][a-z]+\s+)?(?:It|They|This|These|You|We|The)\b)"
        r"[A-Za-z][\w'-]*(?:\s+[\w'-]+){0,3},\s+"
        r"[\w'-]+(?:\s+[\w'-]+){0,3},\s+"
        r"[\w'-]+(?:\s+[\w'-]+){0,5}\.\s*$",
    ),
    # A business function doing a human verb: "product quality gets the record".
    "org-chart-actor": re.compile(
        r"\b(?:product quality|quality|compliance|finance|legal|risk|procurement|operations|underwriting|engineering|the business)\s+"
        r"(?:gets?|hears?|learns?|sees?|asks?|knows?|remembers?|feels?|is told)\b",
        re.IGNORECASE,
    ),
    # Systems vocabulary leaking into reader-facing prose.
    "insider-jargon": re.compile(
        r"\b(?:read-only|write-back|system of record|source of truth|golden record|"
        r"swivel-chair|human-in-the-loop|state machine|payload|upsert|idempoten\w*)\b",
        re.IGNORECASE,
    ),
    # A screen, app, map or row doing a human verb with attitude. "show",
    # "list" and "mark" are deliberately absent: those are what screens do.
    "interface-as-narrator": re.compile(
        r"\b(?:the\s+(?:app|map|screen|page|record|ledger|dashboard|diagram|report|row|table|tool|system|estate"
        r"|recommendation|finding|proposal|rationale|brief)|it)\s+"
        r"(?:says|admits?|keeps\s+score|refuses?|tells\s+us|insists?|announces?|wants|knows\s+best|reads\s+itself"
        r"|splits?|decides?)\b",
        re.IGNORECASE,
    ),
    # A sentence that defines a thing as itself.
    "circular-assertion": re.compile(
        r"\bthe\s+(\w+)\b[^.!?]{0,60}?\b(?:are|is)\s+(?:these|those|that|the\s+same)\s+\1\b",
        re.IGNORECASE,
    ),
    # Counting UI containers instead of reading them.
    "furniture-inventory": re.compile(
        r"\b(?:two|three|four|five|several|a\s+few)\s+(?:cards?|tiles?|panels?|widgets?|chips?)\s*:",
        re.IGNORECASE,
    ),
    # The script talking about the talk.
    "speaker-meta": re.compile(
        r"\b(?:easy\s+to\s+(?:mix\s+up|confuse)|hold\s+that\s+(?:pattern|thought)|"
        r"(?:as|what)\s+we\s+saw\s+in\s+act\s+[ivx\d]+|this\s+whole\s+(?:story|talk|demo)\s+is\s+about)\b",
        re.IGNORECASE,
    ),
    # Compressed ad-copy rhythm in place of a spoken sentence.
    "trailer-cadence": re.compile(
        r"\bOne\s+(?:glance|click|look|tap|button)\s+and\b",
        re.IGNORECASE,
    ),
    # The prose rates its subject instead of showing it.
    "announced-virtue": re.compile(
        r"(?:\b(?:and|but)\s+it\s+is\s+(?:honest|useful|important|clear|simple|elegant|powerful|remarkable)\b"
        r"|\bthe\s+(?:useful|important|interesting|striking)\s+(?:thing|part)\s+(?:about|here)\b"
        r"|\bthat\s+matters\s+more\s+than\s+it\s+sounds\b)",
        re.IGNORECASE,
    ),
    "mechanism-speak": re.compile(
        r"\b(?:sits?|stays?|lives?|accumulates?)\s+(?:on|in)\s+(?:one|the same)\s+\w+",
        re.IGNORECASE,
    ),
}


def scan(text: str) -> list[dict[str, object]]:
    findings: list[dict[str, object]] = []
    for line_number, line in enumerate(text.splitlines(), start=1):
        for name, pattern in PATTERNS.items():
            matches = list(pattern.finditer(line))
            if name == "dash-cluster" and len(matches) < 2:
                continue
            for match in matches:
                findings.append(
                    {
                        "pattern": name,
                        "line": line_number,
                        "excerpt": match.group(0),
                    }
                )
    return findings


HEDGE_MARKERS = re.compile(
    r"\b(?:although|though|however|while|whereas|because|since|unless|"
    r"which|whether|perhaps|arguably|somewhat|may|might|could|"
    r"seems?|tends? to|in some cases|to some extent|it is possible)\b",
    re.IGNORECASE,
)


def _split_sentences(paragraph: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", paragraph.strip()) if s.strip()]


def _sentence_shape(sentence: str) -> str:
    """Compound/hedged carries a subordinate clause or a hedge word; simple does not."""
    has_hedge = bool(HEDGE_MARKERS.search(sentence))
    has_comma_clause = "," in sentence
    word_count = len(sentence.split())
    if has_hedge or (has_comma_clause and word_count > 14):
        return "compound"
    return "simple"


def scan_sentence_shape(text: str, *, run_threshold: int = 4) -> list[dict[str, object]]:
    """Flag a run of consecutive same-shape sentences within one paragraph.

    A single hedged or single short sentence is ordinary prose; this only fires
    on a run, matching the catalog's "Clause-shape monotony" entry.
    """
    findings: list[dict[str, object]] = []
    for para_index, paragraph in enumerate(re.split(r"\n\s*\n", text), start=1):
        sentences = _split_sentences(paragraph)
        if len(sentences) < run_threshold:
            continue
        shapes = [_sentence_shape(s) for s in sentences]
        run_shape, run_len, run_start = shapes[0], 1, 0
        for i in range(1, len(shapes) + 1):
            if i < len(shapes) and shapes[i] == run_shape:
                run_len += 1
                continue
            if run_len >= run_threshold:
                findings.append(
                    {
                        "pattern": "sentence-shape-run",
                        "paragraph": para_index,
                        "shape": run_shape,
                        "run_length": run_len,
                        "excerpt": " ".join(sentences[run_start : run_start + run_len])[:160],
                    }
                )
            if i < len(shapes):
                run_shape, run_len, run_start = shapes[i], 1, i
    return findings


NUMBER_TOKEN = re.compile(
    r"\b(?:\d[\d,.]*%?|zero|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|"
    r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|"
    r"eighty|ninety|hundred|thousand|million)\b",
    re.IGNORECASE,
)

TURN_MARKERS = re.compile(
    r"\b(?:but|though|instead|yet|except|until|unless|because|so that|which|who|that is|"
    r"and then|now|no longer|used to)\b|[:;]",
    re.IGNORECASE,
)

IMPERATIVE_START = re.compile(
    r"^(?:and\s+|so\s+|then\s+)?(?:look|notice|watch|see|take|point|open|click|say|read|"
    r"imagine|picture|consider|remember|start|keep)\b",
    re.IGNORECASE,
)

AUXILIARY = re.compile(
    r"\b(?:is|are|was|were|be|been|being|am|has|have|had|does|do|did|"
    r"can|could|will|would|shall|should|must|may|might)\b",
    re.IGNORECASE,
)


def _is_beat(sentence: str) -> bool:
    """A fragment or an imperative is a pointing beat, not a flat declarative.

    Short-short-short-long is what the spoken register asks for, so a run broken
    by a label fragment ("Two departments, stitched into one flow.") or an
    imperative ("And look at substitution.") is tempo rather than a recited list.
    """
    if IMPERATIVE_START.match(sentence.strip()):
        return True
    # A verbless label reads as a beat. Detecting "no verb" without a parser is
    # unreliable, so use the shape these actually take: a noun phrase, a comma,
    # and no auxiliary or copula anywhere ("Two departments, stitched into one
    # flow."). A plain declarative carries no comma or carries an auxiliary.
    return "," in sentence and not AUXILIARY.search(sentence)


def scan_flat_declarative_run(
    text: str, *, run_threshold: int = 3, spread: int = 4
) -> list[dict[str, object]]:
    """Flag consecutive sentences of near-identical length that none of them turns.

    The catalog's "Clause-shape monotony" covers the hedged run; this covers the
    one writers miss, where every sentence is short, correct and the same size,
    so the paragraph reads as a list being recited. Sentences that carry a turn
    (a contrast, a subordinate move, a colon) break the run, because that is the
    fix the catalog asks for.
    """
    findings: list[dict[str, object]] = []
    for para_index, paragraph in enumerate(re.split(r"\n\s*\n", text), start=1):
        sentences = _split_sentences(paragraph)
        if len(sentences) < run_threshold:
            continue
        run: list[str] = []

        def flush(run: list[str]) -> None:
            if len(run) < run_threshold:
                return
            counts = [len(s.split()) for s in run]
            if max(counts) - min(counts) > spread:
                return
            findings.append(
                {
                    "pattern": "flat-declarative-run",
                    "paragraph": para_index,
                    "run_length": len(run),
                    "word_counts": counts,
                    "excerpt": " ".join(run)[:160],
                }
            )

        for sentence in sentences:
            if TURN_MARKERS.search(sentence) or _is_beat(sentence):
                flush(run)
                run = []
                continue
            run.append(sentence)
        flush(run)
    return findings


ROUNDING_CUE = re.compile(
    r"(?:call it|close to|about|around|roughly|nearly|almost|some|over|under|"
    r"more than|less than|getting on for|the better part of|a dozen|dozens)\s+(?:a|an|the)?\s*$",
    re.IGNORECASE,
)


PRONOMINAL_ONE = re.compile(
    r"(?:\b(?:each|every|not|any|no|the|this|that|another|which|only)\s+one\b"
    r"|\bone\s+of\b)",
    re.IGNORECASE,
)

IDENTIFIER = re.compile(r"[A-Za-z]-?\d|\d-?[A-Za-z]")

ELAPSED_MARKER = re.compile(
    r"\b\w+\s+(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\s+"
    r"(?:on|later|ago|in|before|after)\b",
    re.IGNORECASE,
)


def _has_exact_figure(sentence: str) -> bool:
    """A figure counts as exact unless the speaker audibly rounded it.

    "call it forty" and "close to a hundred" are the catalog's prescribed fix,
    so counting them as precision would flag the repair as the defect.
    """
    for match in NUMBER_TOKEN.finditer(sentence):
        token = match.group(0)
        before = sentence[: match.start()]
        after = sentence[match.end() :]
        if ROUNDING_CUE.search(before):
            continue
        if after.lower().startswith(" or so"):
            continue
        # "each one", "one of them": the pronoun, not a count
        window = (before[-12:] + token + after[:6])
        if token.lower() == "one" and PRONOMINAL_ONE.search(window):
            continue
        # SR-440, WR-2026-0417: an identifier the room reads, not a quantity
        if IDENTIFIER.search(sentence[max(0, match.start() - 2) : match.end() + 2]):
            continue
        # "six months on", "three months later": a time marker, not data
        if ELAPSED_MARKER.match(sentence[match.start() :]):
            continue
        return True
    return False


def scan_stacked_precision(
    text: str, *, run_threshold: int = 3
) -> list[dict[str, object]]:
    """Flag a run of consecutive sentences that each land an exact figure.

    Any one of them is fine. Three in a row cannot be heard, which is what makes
    this a spoken-register problem before it is a prose problem. Audibly rounded
    figures do not count, because rounding is the fix.
    """
    findings: list[dict[str, object]] = []
    for para_index, paragraph in enumerate(re.split(r"\n\s*\n", text), start=1):
        sentences = _split_sentences(paragraph)
        run, run_start = 0, 0
        for i, sentence in enumerate(sentences + [""]):
            if sentence and _has_exact_figure(sentence):
                if run == 0:
                    run_start = i
                run += 1
                continue
            if run >= run_threshold:
                findings.append(
                    {
                        "pattern": "stacked-precision",
                        "paragraph": para_index,
                        "run_length": run,
                        "excerpt": " ".join(sentences[run_start : run_start + run])[:160],
                    }
                )
            run = 0
    return findings


SPOKEN_PATTERNS = {
    # "a clock, a warning when it is at risk and an escalation when it breaches"
    "compressed-mechanism": re.compile(
        r"\ba\s+\w+(?:\s+\w+){0,2},\s+(?:a|an)\s+\w+(?:\s+\w+){0,3}\s+when\b[^.]{0,60}?\band\s+(?:a|an)\s+\w+",
        re.IGNORECASE,
    ),
    # "hand it that", "give them that one" - two object pronouns nobody can say
    "stacked-object-pronouns": re.compile(
        r"\b(?:hand|give|send|show|pass|tell)\s+(?:it|them|him|her|us)\s+(?:that|this|those|these|it|one)\b",
        re.IGNORECASE,
    ),
}

PARAGRAPH_OPENER = re.compile(
    r"^(?:It|They|That one|Those|This one)\b(?!\s+(?:is|was|are|were)\s+(?:the|a|an)\b)",
)


def scan_spoken(text: str) -> list[dict[str, object]]:
    """Checks that only make sense for a piece someone will say out loud.

    Narrow on purpose. Each of these was measured against a 40-piece talk-track
    set before shipping: the three here fired only on true positives, and a
    fourth candidate (a verbless comma inventory) fired three times, all false,
    because that is also the shape of a legitimate pointing beat. The wider
    "compressed mechanism" judgment stays unlinted - see the catalog's
    **Telegraphic speech**, which explains why.
    """
    findings: list[dict[str, object]] = []
    for name, pattern in SPOKEN_PATTERNS.items():
        for match in pattern.finditer(text):
            findings.append(
                {
                    "pattern": name,
                    "line": text[: match.start()].count("\n") + 1,
                    "excerpt": match.group(0)[:120],
                }
            )
    for para_index, paragraph in enumerate(re.split(r"\n\s*\n", text), start=1):
        first = paragraph.strip()
        if para_index > 1 and PARAGRAPH_OPENER.match(first):
            findings.append(
                {
                    "pattern": "paragraph-opens-on-pronoun",
                    "paragraph": para_index,
                    "excerpt": first[:120],
                }
            )
    return findings


def scan_em_dash(text: str, *, max_per_100_words: float = 1.0) -> list[dict[str, object]]:
    """Flag em dash overuse by density across the whole piece, never a single instance.

    One em dash in a short passage is the guardrails' "used once, deliberately"
    case and must not fire; this only reports when the piece leans on it as a
    default connector.
    """
    words = len(re.findall(r"\S+", text))
    count = text.count("—")
    if words == 0 or count < 2:
        return []
    density = count / words * 100
    if density <= max_per_100_words:
        return []
    return [
        {
            "pattern": "em-dash-overuse",
            "count": count,
            "words": words,
            "density_per_100_words": round(density, 2),
            "excerpt": f"{count} em dashes across {words} words",
        }
    ]


def scan_set(text: str, *, share: float = 0.2) -> list[dict[str, object]]:
    """Measure a set of pieces against itself, not each piece against the rules.

    Editing many pieces to one standard installs the standard as the next
    pattern, and the writer of the set is the last person able to see it. The
    catalog asks for this measurement; without it the check is guesswork. Pieces
    are blank-line separated. Anything shared by more than `share` of the set is
    a finding whatever its quality in isolation - the usual one is an article,
    left behind after a pass that varied the verbs.
    """
    pieces = [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]
    if len(pieces) < 8:
        return []
    threshold = max(2, math.ceil(len(pieces) * share))
    findings: list[dict[str, object]] = []

    def first_word(piece: str) -> str:
        words = re.findall(r"[\w'-]+", piece)
        return words[0].lower() if words else ""

    def last_words(piece: str) -> str:
        words = re.findall(r"[\w'-]+", piece)
        return " ".join(w.lower() for w in words[-2:])

    for label, key in (("opening word", first_word), ("closing words", last_words)):
        counts = Counter(key(p) for p in pieces if key(p))
        for value, n in counts.most_common():
            if n < threshold:
                break
            findings.append({
                "pattern": f"set-uniform-{label.split()[0]}",
                "excerpt": (f"{n} of {len(pieces)} pieces share the {label} "
                            f"\"{value}\" (threshold {threshold})"),
            })

    # The catalog names opening words, connectives and the shape of the closing
    # clause. Length is deliberately not measured: short pieces cluster in a
    # narrow band for honest reasons, and an early version of this check fired
    # on a set that had just been varied on purpose.
    connectives = ("instead of", "rather than", "not just", "which means",
                   "so that", "in order to", "as well as", "the point is")
    for phrase in connectives:
        n = sum(1 for p in pieces if phrase in p.lower())
        if n >= threshold:
            findings.append({
                "pattern": "set-uniform-connective",
                "excerpt": (f"{n} of {len(pieces)} pieces lean on \"{phrase}\" "
                            f"(threshold {threshold}); a pass that removed one "
                            "construction usually installed this one"),
            })
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Flag selected natural-writing review prompts without judging authorship."
    )
    parser.add_argument("path", type=Path)
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument(
        "--spoken",
        action="store_true",
        dest="as_spoken",
        help="add the checks that only apply to a piece meant to be said out "
             "loud: compressed mechanisms, stacked object pronouns, and a "
             "paragraph opening on a pronoun the listener must resolve",
    )
    parser.add_argument(
        "--set",
        action="store_true",
        dest="as_set",
        help="treat blank-line separated blocks as one set and measure them "
             "against each other, per the catalog's Editing a set",
    )
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    findings = scan(text)
    whole_piece_findings = (
        scan_em_dash(text)
        + scan_sentence_shape(text)
        + scan_flat_declarative_run(text)
        + scan_stacked_precision(text)
    )
    if args.as_spoken:
        whole_piece_findings += scan_spoken(text)
    if args.as_set:
        whole_piece_findings += scan_set(text)
    if args.as_json:
        print(json.dumps(findings + whole_piece_findings, indent=2))
    else:
        for finding in findings:
            print(f"{finding['line']}: {finding['pattern']}: {finding['excerpt']}")
        for finding in whole_piece_findings:
            print(f"{finding['pattern']}: {finding['excerpt']}")
        if not findings and not whole_piece_findings:
            print("No configured high-signal patterns found.")
    return 1 if (findings or whole_piece_findings) else 0


if __name__ == "__main__":
    raise SystemExit(main())
