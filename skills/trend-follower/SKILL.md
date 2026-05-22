---
name: trend-follower
description: Find fast-rising open-source GitHub projects from the past week and explain what they do. Use when the user invokes `/trendfollower`, `/trendfollower 1`, `/trendfollower 2`, `/trendfollower 1 agent`, `/trendfollower 2 20 coding tools`, asks for GitHub projects with the fastest star growth over the last 7 days or this week, asks for weekly GitHub Trending summaries, or wants an exportable Markdown report of ranked projects. Mode 1 ranks by absolute stars gained in the past week. Mode 2 ranks by 7-day percentage star growth. Optional trailing words are treated as a topic or keyword scope.
---

# Trend Follower

## Overview

Produce a current, source-backed ranking of fast-growing open-source GitHub repositories and save a reusable Markdown report. The scan may be global or constrained to an optional topic/keyword scope. Always show the result in chat and, when file access is available, prefer overwriting `~/Documents/Codex/TrendFollower/trend-follower.md` with the same report.

## Command Protocol

Recognize these slash-style prompts as direct invocations:

- `/trendfollower`
- `/trendfollower 1`
- `/trendfollower 2`
- `/trendfollower 1 <count>`
- `/trendfollower 2 <count>`
- `/trendfollower <topic>`
- `/trendfollower 1 <topic>`
- `/trendfollower 2 <topic>`
- `/trendfollower 1 <count> <topic>`
- `/trendfollower 2 <count> <topic>`

Interpret the first numeric argument as the ranking mode:

- `1`: Default. Rank by absolute stars gained over the past week.
- `2`: Rank by 7-day percentage star growth.

Parse arguments left to right after `/trendfollower`:

1. If the first token is exactly `1` or `2`, use it as the ranking mode and consume it. If the first token is another pure integer, explain that only modes `1` and `2` are supported and offer to continue with mode `1`.
2. After the optional mode, if the next token is a positive pure integer, use it as the result count and consume it.
3. Treat all remaining tokens as the topic/keyword scope, preserving their order and wording. Tokens that start with digits but are not pure integers, such as `3D`, are topic text.

If the mode is omitted, use mode `1`. If the count is omitted, use `10`. Examples:

- `/trendfollower agent`: mode `1`, count `10`, topic `agent`.
- `/trendfollower 1 agent`: mode `1`, count `10`, topic `agent`.
- `/trendfollower 2 20 coding tools`: mode `2`, count `20`, topic `coding tools`.
- `/trendfollower 1 20 3D`: mode `1`, count `20`, topic `3D`.

## Workflow

1. Parse the user request for mode, result count, language, optional topic/keyword scope, and any special source preferences.
2. Gather fresh data. For current weekly rankings, browse/search live sources; do not rely on a stale remembered list.
3. Apply the mode-specific and topic-specific source policy from `references/source-policy.md`.
4. If a topic is provided, first find topic-relevant repositories or topic-relevant trend pages when possible, then rank the resulting candidates using the selected metric. If the only available ranking source is global, rank by the selected metric first, then filter for topic relevance and label that limitation clearly.
5. Verify each repository is open source and identify its purpose from the repo description, README, or project homepage.
6. Produce the chat answer with the required metadata and table.
7. When local file access is available, write the full Markdown report to the output location described below. Do not write reports into the installed skill directory unless the user explicitly asks for that path. Do not create timestamped or per-test files unless the user explicitly asks for historical reports.

## Runtime Budget

TrendFollower is intended to be a fast discovery workflow, not an exhaustive research job. Aim to finish in under 3 minutes and stop expanding the search before 5 minutes.

- Prefer a useful partial ranking with transparent limitations over a slow attempt to fill every requested row.
- For topic-scoped runs, use at most one source-native topic/language page plus a small number of high-signal ranking/search pages before producing the report.
- Verify only repositories that will appear in the ranked table or `Additional Candidates`; do not deeply inspect every raw candidate.
- Use repository descriptions, visible GitHub metadata, license metadata, and README snippets before opening full project pages. If open-source status or topic relevance cannot be verified quickly, exclude the repository or move it to `Additional Candidates` with a clear reason.
- If the ranked result count is below the requested count when the budget is reached, report the smaller ranked set and optionally add up to 5 `Additional Candidates`.
- Mention in `Limitations` when the result is partial because the fast runtime budget prevented a broader search.

## Required Metadata

Every chat answer and report file must include:

- Query date.
- Ranking mode.
- Topic/scope. Use `Global` when no topic is provided.
- Sorting metric.
- Data source names and links where possible.
- Scope and limitations, especially whether the source is topic-specific, keyword-filtered, post-filtered from a global ranking, a weekly calendar/trending view, or a strict rolling 168-hour measurement.

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

`/trendfollower 1 agent`

Use mode `1`, return 10 projects related to `agent`, rank topic-relevant candidates by weekly absolute stars gained, show the table in chat, and overwrite `outputs/trend-follower.md`.

`/trendfollower 2 20 3D`

Use mode `2`, return 20 projects related to `3D`, rank topic-relevant candidates by 7-day percentage star growth where the source supports it, show the table in chat, and overwrite `outputs/trend-follower.md`.
