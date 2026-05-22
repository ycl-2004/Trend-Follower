# Output Format

## Chat Answer

Use the user's language when practical. Keep the chat answer readable and include:

```text
Query date: YYYY-MM-DD
Mode: 1 - absolute stars gained, or 2 - percentage growth
Topic: Global, or the requested topic/keyword scope
Sorting metric: ...
Sources: ...
Scope: ...
Limitations: ...
Report file: ~/Documents/Codex/TrendFollower/trend-follower.md
```

Then provide one table:

| Rank | Project | Growth | Purpose | Source |
|---:|---|---:|---|---|
| 1 | owner/repo | +12,345 stars | One-sentence purpose. | Source link |

If a topic-filtered search finds relevant repositories that lack supportable weekly growth data or if the ranked table has fewer results than requested, add a short optional `Additional Candidates` section after the ranked table:

| Project | Reason not ranked | Purpose | Source |
|---|---|---|---|
| owner/repo | Relevant open-source project found by broader GitHub search, not a weekly trend result. | One-sentence purpose. | Source link |

## Markdown Report

Write the full report to `~/Documents/Codex/TrendFollower/trend-follower.md` and overwrite the previous file. If that path is not writable, use `outputs/trend-follower.md` in the current workspace and say that the fallback path was used.

```md
# TrendFollower Report

Query date: YYYY-MM-DD  
Mode: 1  
Topic: Global  
Sorting metric: Absolute stars gained in the past week  
Sources: GitHub Trending weekly  
Scope: Global weekly repository scan  
Limitations: GitHub Trending's "this week" view may not equal a strict rolling 168-hour period.

| Rank | Project | Growth | Purpose | Source |
|---:|---|---:|---|---|
| 1 | [owner/repo](https://github.com/owner/repo) | +12,345 stars | One-sentence purpose. | [GitHub Trending](https://github.com/trending?since=weekly) |
```

For a topic-filtered run, set `Topic:` to the user's topic and use `Scope:` to identify how the topic was applied, for example `GitHub repository search candidate set, ranked by weekly star gain` or `Post-filtered from a global weekly ranking`.

When relevant topic candidates cannot be ranked because growth data is missing, or when broader open-source search finds useful topic matches outside the weekly trend data, include them below the ranked table under `Additional Candidates`. Do not mix them into the ranked table.

If the fast runtime budget prevents filling the requested count, say that plainly in `Limitations`, for example: `Fast runtime budget reached after checking the highest-signal sources, so the ranked table has fewer than the requested 10 results.`

## File Rules

- Default output directory: `~/Documents/Codex/TrendFollower/`
- Default output file: `~/Documents/Codex/TrendFollower/trend-follower.md`
- Fallback output file: `outputs/trend-follower.md` in the current workspace
- Overwrite the file on every run.
- Do not write generated reports into the installed skill directory unless the user explicitly asks for that path.
- Do not create `test1.md`, `test2.md`, timestamped files, or history files in normal use.
- During local validation, temporary test files may be created and must be deleted before the workspace is considered clean.
