#!/usr/bin/env python3
"""Render a TrendFollower Markdown report from structured JSON results."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
from typing import Any


MODE_LABELS = {
    "1": "Absolute stars gained in the past week",
    "2": "7-day percentage star growth",
}

GLOBAL_TOPIC_LABEL = "Global"
GLOBAL_SCOPE_LABEL = "Global weekly repository scan"
TOPIC_SCOPE_LABEL = (
    "Topic-filtered repository scan using the provided topic or keywords"
)


def escape_cell(value: Any) -> str:
    text = "" if value is None else str(value)
    return text.replace("|", "\\|").replace("\n", " ").strip()


def project_cell(item: dict[str, Any]) -> str:
    repo = escape_cell(item.get("repo") or item.get("project") or "")
    url = item.get("url") or item.get("repo_url")
    if url:
        return f"[{repo}]({escape_cell(url)})"
    return repo


def source_cell(item: dict[str, Any]) -> str:
    source = escape_cell(item.get("source") or "Source")
    url = item.get("source_url")
    if url:
        return f"[{source}]({escape_cell(url)})"
    return source


def load_report_data(path: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    if path == "-":
        raw = sys.stdin.read()
    else:
        raw = pathlib.Path(path).read_text(encoding="utf-8")

    data = json.loads(raw)
    unranked_items: list[dict[str, Any]] = []
    if isinstance(data, dict):
        items = data.get("items", [])
        unranked_items = data.get("unranked_items", data.get("unranked", []))
    else:
        items = data
    if not isinstance(items, list):
        raise SystemExit("Input JSON must be a list or an object with an 'items' list.")
    if not isinstance(unranked_items, list):
        raise SystemExit("'unranked_items' must be a list when provided.")
    return items, unranked_items


def render(
    args: argparse.Namespace,
    items: list[dict[str, Any]],
    unranked_items: list[dict[str, Any]],
) -> str:
    topic = args.topic.strip() if args.topic else GLOBAL_TOPIC_LABEL
    scope = args.scope.strip() if args.scope else (
        GLOBAL_SCOPE_LABEL if topic == GLOBAL_TOPIC_LABEL else TOPIC_SCOPE_LABEL
    )
    lines = [
        "# TrendFollower Report",
        "",
        f"Query date: {args.query_date}  ",
        f"Mode: {args.mode}  ",
        f"Topic: {topic}  ",
        f"Sorting metric: {MODE_LABELS[args.mode]}  ",
        f"Sources: {args.sources}  ",
        f"Scope: {scope}  ",
        f"Limitations: {args.limitations}",
        "",
        "| Rank | Project | Growth | Purpose | Source |",
        "|---:|---|---:|---|---|",
    ]

    for index, item in enumerate(items, start=1):
        lines.append(
            "| {rank} | {project} | {growth} | {purpose} | {source} |".format(
                rank=index,
                project=project_cell(item),
                growth=escape_cell(item.get("growth", "")),
                purpose=escape_cell(item.get("purpose", "")),
                source=source_cell(item),
            )
        )

    if unranked_items:
        lines.extend(
            [
                "",
                "## Additional Candidates",
                "",
                "These repositories matched the requested topic but were not included in the ranking because they were found outside the supported weekly growth data.",
                "",
                "| Project | Reason not ranked | Purpose | Source |",
                "|---|---|---|---|",
            ]
        )
        for item in unranked_items:
            lines.append(
                "| {project} | {reason} | {purpose} | {source} |".format(
                    project=project_cell(item),
                    reason=escape_cell(
                        item.get("reason")
                        or item.get("reason_not_ranked")
                        or "Relevant open-source project found by broader GitHub search, not a weekly trend result."
                    ),
                    purpose=escape_cell(item.get("purpose", "")),
                    source=source_cell(item),
                )
            )

    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Render a TrendFollower Markdown report from structured JSON results."
    )
    parser.add_argument("--input", default="-", help="JSON input path, or '-' for stdin.")
    parser.add_argument(
        "--output", default="~/Documents/Codex/TrendFollower/trend-follower.md"
    )
    parser.add_argument("--mode", choices=sorted(MODE_LABELS), default="1")
    parser.add_argument("--query-date", default=dt.date.today().isoformat())
    parser.add_argument(
        "--topic",
        default="",
        help="Optional topic or keyword scope. Defaults to Global.",
    )
    parser.add_argument(
        "--scope",
        default="",
        help="Optional description of how the topic or global scope was applied.",
    )
    parser.add_argument("--sources", required=True)
    parser.add_argument("--limitations", required=True)
    args = parser.parse_args()

    items, unranked_items = load_report_data(args.input)
    report = render(args, items, unranked_items)

    output_path = pathlib.Path(args.output).expanduser()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
