<p align="center">
  <img src="img/Banner.png" alt="TrendFollower banner" width="100%">
</p>

# TrendFollower

TrendFollower is a Codex skill for finding fast-rising open-source GitHub projects from the past week. It supports a slash-style prompt convention:

```text
/trendfollower
/trendfollower 1
/trendfollower 2
/trendfollower 1 20
/trendfollower 2 20
```

Mode `1` is the default and ranks projects by absolute stars gained over the past week. Mode `2` ranks by 7-day percentage star growth.

## Install

Clone the repository and copy the skill into your Codex skills directory:

```bash
git clone https://github.com/ycl-2004/Trend-Follower.git
mkdir -p ~/.codex/skills
cp -R Trend-Follower/skills/trend-follower ~/.codex/skills/
```

Restart Codex after installing so the skill can be discovered.

## Usage

Ask Codex:

```text
/trendfollower
```

or:

```text
/trendfollower 2 20
```

The skill always returns the result in chat. When file access is available, it also overwrites:

```text
outputs/trend-follower.md
```

The report includes the query date, data sources, ranking metric, known limitations, and a Markdown table of the ranked repositories.

## Slash-Style Invocation

Installing this skill makes Codex aware of the `trend-follower` workflow. In v1, `/trendfollower` is treated as a slash-style prompt that the skill description is designed to recognize; it is not a separate Codex slash command registration and may not appear in a slash-command menu.

If your Codex environment supports custom slash commands, you can add a command wrapper later that forwards to this skill. The skill itself still works when the user types `/trendfollower`, `/trendfollower 1`, or `/trendfollower 2` as a normal message.

## Dependencies

Normal usage requires:

- Codex with skill discovery enabled.
- Internet/search access for fresh public GitHub ranking data.
- Workspace file access if you want `outputs/trend-follower.md` to be written.

The GitHub connector/plugin is not required for the default public ranking workflow. It can be useful for authenticated GitHub API access, private repositories, PR/issue workflows, or higher-rate programmatic GitHub operations, but `/trendfollower` only needs public web access for sources such as GitHub Trending weekly and credible public star-growth leaderboards.

Python is optional. The included `scripts/render_report.py` helper uses only the Python standard library and is useful when Codex has structured result data to write into a Markdown report. The skill can still produce the chat answer and Markdown file without that script.

Development validation is the only part that may require an extra Python package: the official `quick_validate.py` script imports `PyYAML`. Install `PyYAML` only if your Python environment does not already include it and you want to run that validator.

## Project Structure

```text
skills/
  trend-follower/
    SKILL.md
    agents/openai.yaml
    references/source-policy.md
    references/output-format.md
    scripts/render_report.py
outputs/
  .gitkeep
```

The `outputs/` directory is for generated reports. Markdown report files in that directory are intentionally ignored so local runs do not pollute the repository.

## Validate

Run the skill validator. The validator imports `PyYAML`; install it first if your Python environment does not already have it.

```bash
python3 /Users/yichenlin/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/trend-follower
```

Smoke-test the report formatter:

```bash
printf '[{"repo":"owner/repo","url":"https://github.com/owner/repo","growth":"+100 stars","purpose":"Example project.","source":"Fixture","source_url":"https://example.com"}]' | python3 skills/trend-follower/scripts/render_report.py --mode 1 --sources "Fixture" --limitations "Fixture data for local testing only." --output outputs/trend-follower.md
```

Delete `outputs/trend-follower.md` after local smoke tests if you want a clean publishing workspace.
