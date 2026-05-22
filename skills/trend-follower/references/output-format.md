# Output Format

## Chat Answer

Use the user's language when practical. Keep the chat answer readable and include:

```text
Query date: YYYY-MM-DD
Mode: 1 - absolute stars gained, or 2 - percentage growth
Sorting metric: ...
Sources: ...
Limitations: ...
Report file: ~/Documents/Codex/TrendFollower/trend-follower.md
```

Then provide one table:

| Rank | Project | Growth | Purpose | Source |
|---:|---|---:|---|---|
| 1 | owner/repo | +12,345 stars | One-sentence purpose. | Source link |

## Markdown Report

Write the full report to `~/Documents/Codex/TrendFollower/trend-follower.md` and overwrite the previous file. If that path is not writable, use `outputs/trend-follower.md` in the current workspace and say that the fallback path was used.

```md
# TrendFollower Report

Query date: YYYY-MM-DD  
Mode: 1  
Sorting metric: Absolute stars gained in the past week  
Sources: GitHub Trending weekly  
Limitations: GitHub Trending's "this week" view may not equal a strict rolling 168-hour period.

| Rank | Project | Growth | Purpose | Source |
|---:|---|---:|---|---|
| 1 | [owner/repo](https://github.com/owner/repo) | +12,345 stars | One-sentence purpose. | [GitHub Trending](https://github.com/trending?since=weekly) |
```

## File Rules

- Default output directory: `~/Documents/Codex/TrendFollower/`
- Default output file: `~/Documents/Codex/TrendFollower/trend-follower.md`
- Fallback output file: `outputs/trend-follower.md` in the current workspace
- Overwrite the file on every run.
- Do not write generated reports into the installed skill directory unless the user explicitly asks for that path.
- Do not create `test1.md`, `test2.md`, timestamped files, or history files in normal use.
- During local validation, temporary test files may be created and must be deleted before the workspace is considered clean.
