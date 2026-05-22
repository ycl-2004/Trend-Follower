# Source Policy

## Mode 1: Absolute Stars Gained

Use mode `1` for `/trendfollower`, `/trendfollower 1`, and natural-language requests such as "fastest-growing GitHub projects this week" when the user does not specify percentage growth.

Preferred sources:

1. GitHub Trending with the weekly time range, when it exposes "stars this week" values.
2. A credible star-growth leaderboard that publishes 7-day absolute star gains.
3. GitHub repository data plus a credible third-party time-series source when the ranking source is incomplete.

State the time-window limitation. GitHub Trending's "this week" view is a weekly/trending window and may not equal a strict rolling 168-hour period.

## Mode 2: Percentage Growth

Use mode `2` for `/trendfollower 2` or when the user explicitly asks for percentage growth.

Preferred sources:

1. A credible 7-day percentage-growth leaderboard such as RepoFOMO or an equivalent source that documents its ranking metric.
2. A source that provides both current stars and 7-day start/end stars, allowing the percentage to be calculated.

If the source has a minimum-star threshold, category filter, or excludes archived/private/forked repositories, state that limitation.

## Topic And Keyword Scoping

When the user provides trailing topic text, treat it as the scan scope before ranking whenever the source allows it.

Keep topic scoping fast. Do not search every possible language, topic, or third-party leaderboard. Use the first sufficiently credible source path that yields a useful ranked set, then stop.

Preferred topic workflow:

1. Look for an official or source-native topic/language/trending page that matches the topic, such as a GitHub Trending weekly language page for programming languages or a GitHub topic page for a named ecosystem.
2. If no topic-specific trend page exists, use GitHub repository search to find candidate repositories matching the topic or keywords. Prefer structured filters such as `topic:<topic>`, `in:topics`, `in:name,description`, `in:readme`, and `language:<language>` when they match the user's wording. Confirm candidates are public repositories.
3. Rank the candidate repositories using the selected mode's metric. For mode `1`, prefer sources that publish weekly absolute star gains. For mode `2`, prefer sources that publish 7-day percentage growth or enough start/end star data to calculate it.
4. If a ranking source only provides a global weekly list, apply the selected ranking first, then filter the ranked repositories for topic relevance. Clearly label this as a post-filtered global ranking.
5. If the topic search finds relevant repositories but no weekly growth source for some of them, include only the repositories with supportable growth data in the ranked table. Add the other relevant repositories to an optional `Additional Candidates` section and clearly state that they matched the topic but were not ranked because supported growth data was unavailable.
6. If a topic-filtered ranking returns fewer repositories than the requested count, it is acceptable to run a broader GitHub open-source search for additional topic-relevant repositories. These additional candidates do not need to be trending this week, but they must be public, open source, and relevant to the requested topic. Keep them outside the ranked table.

For mode `2`, it is acceptable to use a weekly-refreshed percentage-growth source such as RepoFOMO when that is the best available source. State its refresh cadence, minimum-star threshold, category filters, and any shortage of topic-matched results.

Do not present a topic-filtered ranking as complete unless the source actually supports that exact topic scope and metric. The report should say whether the scope came from a source-native topic page, GitHub repository search candidate set, post-filtering of a global ranking, or a broader non-weekly GitHub open-source search for additional candidates.

## Fast Source Limits

Use these limits unless the user explicitly asks for exhaustive research:

- Use no more than 3 broad web searches to discover sources.
- For mode `1`, prefer GitHub Trending weekly pages and stop after a small set of high-signal pages. For broad topics such as `ui`, `agent`, or `coding`, scan no more than 4 ranking pages before producing a partial report.
- For mode `2`, prefer one percentage-growth source first. If it does not expose enough topic matches quickly, report the shortage and use `Additional Candidates` rather than searching many alternative sites.
- Do not open every candidate repository. Verify only the final ranked rows plus optional additional candidates.
- Do not spend time reconciling source disagreements unless they affect a listed result. State the controlling source instead.
- If these limits prevent filling the requested count, return fewer ranked results and say so in `Limitations`.

## Additional Candidates

Use this optional section only when a topic-scoped run cannot fill the requested ranked count or when relevant topic matches lack supportable weekly growth data.

- Do not use additional candidates to fill or reorder the ranked table.
- Search broadly across public GitHub open-source repositories; the candidates do not need to be created, updated, or trending during the current week.
- Verify each candidate is public, open source, and topic-relevant.
- Prefer a small, useful set: default to at most 5 additional candidates and never exceed 10 unless the user explicitly asks for more.
- Explain the reason each candidate was not ranked, such as `No supportable weekly growth data found` or `Relevant open-source project found by broader GitHub search, not a weekly trend result`.

## Verification

For each ranked repository:

- Confirm the repository exists and is public.
- Confirm it is open source when the user asks for open-source projects. Prefer the license shown on GitHub or the repository metadata; do not perform a deep license audit during the fast workflow.
- Confirm why it matches the requested topic when a topic is provided. Prefer repository topics, name, description, README snippet, or official homepage evidence.
- Use the repository description, README snippet, or official project homepage to summarize its purpose.
- Avoid ranking by hype wording or article mentions; rank only by the selected star-growth metric.

## Fallbacks

If live ranking data is unavailable:

1. Say that the live ranking source could not be accessed.
2. Provide the best available partial ranking only if it is clearly labeled.
3. Do not present partial or stale data as definitive.
