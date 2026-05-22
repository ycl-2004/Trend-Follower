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

## Verification

For each ranked repository:

- Confirm the repository exists and is public.
- Confirm it is open source when the user asks for open-source projects. Prefer the license shown on GitHub or the repository metadata.
- Use the repository description, README, or official project homepage to summarize its purpose.
- Avoid ranking by hype wording or article mentions; rank only by the selected star-growth metric.

## Fallbacks

If live ranking data is unavailable:

1. Say that the live ranking source could not be accessed.
2. Provide the best available partial ranking only if it is clearly labeled.
3. Do not present partial or stale data as definitive.
