---
name: trend-follower
description: Find fast-rising open-source GitHub projects from the past week and explain what they do. Use when the user invokes `/trendfollower`, `/trendfollower 1`, `/trendfollower 2`, asks for GitHub projects with the fastest star growth over the last 7 days or this week, asks for weekly GitHub Trending summaries, or wants an exportable Markdown report of the ranked projects. Mode 1 ranks by absolute stars gained in the past week. Mode 2 ranks by 7-day percentage star growth.
---

# Trend Follower

## Overview

Produce a current, source-backed ranking of fast-growing open-source GitHub repositories and save a reusable Markdown report. Always show the result in chat and, when file access is available, prefer overwriting `~/Documents/Codex/TrendFollower/trend-follower.md` with the same report.

## Command Protocol

Recognize these slash-style prompts as direct invocations:

- `/trendfollower`
- `/trendfollower 1`
- `/trendfollower 2`
- `/trendfollower 1 <count>`
- `/trendfollower 2 <count>`

Interpret the first numeric argument as the ranking mode:

- `1`: Default. Rank by absolute stars gained over the past week.
- `2`: Rank by 7-day percentage star growth.

If the mode is omitted, use mode `1`. Interpret the optional second numeric argument as the result count; default to `10`. If the mode is invalid, explain that only `1` and `2` are supported and offer to continue with mode `1`.

## Workflow

1. Parse the user request for mode, result count, language, and any special source preferences.
2. Gather fresh data. For current weekly rankings, browse/search live sources; do not rely on a stale remembered list.
3. Apply the mode-specific source policy from `references/source-policy.md`.
4. Rank the projects using the selected metric and keep only the requested count.
5. Verify each repository is open source and identify its purpose from the repo description, README, or project homepage.
6. Produce the chat answer with the required metadata and table.
7. When local file access is available, write the full Markdown report to the output location described below. Do not write reports into the installed skill directory unless the user explicitly asks for that path. Do not create timestamped or per-test files unless the user explicitly asks for historical reports.

## Required Metadata

Every chat answer and report file must include:

- Query date.
- Ranking mode.
- Sorting metric.
- Data source names and links where possible.
- Scope and limitations, especially whether the source is a weekly calendar/trending view or a strict rolling 168-hour measurement.

## Output File

Default report path:

```text
~/Documents/Codex/TrendFollower/trend-follower.md
```

Overwrite this file on every run. This keeps random project folders clean when the user invokes the skill while working elsewhere.

Fallback report path:

```text
outputs/trend-follower.md
```

Use the fallback only when the default user-level directory is not writable, when the environment only permits writing to the current workspace, or when the user explicitly asks to save the report in the current project. Keep the installed skill directory clean; it should behave like a reusable package, not a per-run output store. Keep the chat answer concise enough to read immediately, but keep the file complete enough to serve as a reference.

Use `references/output-format.md` for the report template. If you have structured result data, `scripts/render_report.py` can write the Markdown report deterministically; otherwise write the same template directly.

## Source And Citation Rules

- Always prefer current sources. This skill is time-sensitive.
- Include direct links or citations for ranking data and repository descriptions when the environment supports them.
- If sources disagree, say which source controlled the ranking and mention the discrepancy.
- If the available source uses a threshold, category filter, or non-rolling time window, state that limitation clearly.
- Do not invent star counts, percentages, licenses, or project purposes.

## Resources

- `references/source-policy.md`: source priority and mode-specific ranking guidance.
- `references/output-format.md`: chat and Markdown report format.
- `scripts/render_report.py`: optional formatter for writing `outputs/trend-follower.md` from structured JSON results.

## Examples

`/trendfollower`

Use mode `1`, return 10 projects, show the table in chat, and overwrite `outputs/trend-follower.md`.

`/trendfollower 2 20`

Use mode `2`, return 20 projects ranked by 7-day percentage star growth, and overwrite `outputs/trend-follower.md`.
