<p align="center">
  <img src="img/Banner.png" alt="TrendFollower banner" width="100%">
</p>

# TrendFollower

TrendFollower 是一个 Codex skill，用来快速发现过去一周 GitHub 上增长较快的开源项目，并用简洁的语言说明每个项目是做什么的。

我做它的原因很简单：现在 AI 工具和开源项目更新太快，很多时候真正浪费时间的不是“看项目”，而是“筛项目”。TrendFollower 希望把这个重复动作整理成一个可以反复调用的 workflow，让用户先得到一个清晰的 overview，再决定哪些项目值得继续打开、测试或学习。

## 它可以做什么

TrendFollower 支持 slash-style 调用：

```text
/trendfollower
/trendfollower 1
/trendfollower 2
/trendfollower 1 20
/trendfollower 2 20
```

模式说明：

- `1`：默认模式，按照过去一周新增 stars 数量排序。
- `2`：按照 7 天百分比增长排序，更适合发现体量不一定最大、但最近增长很快的新项目。
- 最后的数字表示输出数量。例如 `/trendfollower 1 20` 会输出前 20 个项目。

输出内容会尽量包含：

- 项目排名；
- GitHub repository 名称；
- 项目链接；
- 近一周增长数据；
- 项目用途说明；
- 数据来源和当前限制。

## 安装方式

克隆这个 repository，然后把 skill 复制到 Codex 的 skills 目录：

```bash
git clone https://github.com/ycl-2004/Trend-Follower.git
mkdir -p ~/.codex/skills
cp -R Trend-Follower/skills/trend-follower ~/.codex/skills/
```

安装后重启 Codex，让 Codex 重新发现这个 skill。

## 使用方式

在 Codex 中输入：

```text
/trendfollower
```

或者指定模式和数量：

```text
/trendfollower 2 20
```

TrendFollower 会在聊天中直接返回结果。如果当前环境允许写入文件，它也会把完整 Markdown 报告写到默认路径：

```text
~/Documents/Codex/TrendFollower/trend-follower.md
```

如果 Codex 只能写入当前 workspace，或者用户明确要求把报告保存在当前项目里，则使用 fallback 路径：

```text
outputs/trend-follower.md
```

报告文件默认会被覆盖，而不是每次生成新的 timestamp 文件。这样可以保持输出路径稳定，也避免随机污染正在工作的项目目录。

## 关于 slash-style 调用

在当前版本中，`/trendfollower` 是一个 slash-style prompt。也就是说，它是通过 skill description 让 Codex 识别的调用方式，不一定会出现在 Codex 的 slash command 菜单里。

如果你的 Codex 环境支持自定义 slash command，之后也可以再加一个 command wrapper，把真正的 slash command 转发到这个 skill。即使没有 command wrapper，用户直接在聊天中输入 `/trendfollower`、`/trendfollower 1` 或 `/trendfollower 2` 也可以触发这个 workflow。

## 依赖和限制

正常使用需要：

- 支持 skill discovery 的 Codex 环境；
- 可以联网搜索公开 GitHub 趋势数据；
- 如果需要保存报告，需要有文件写入权限。

GitHub connector/plugin 不是默认 workflow 的必需项。TrendFollower 主要依赖公开网页信息，例如 GitHub Trending weekly 和可信的 star-growth 榜单。GitHub connector 可以用于更高额度的 API 访问、私有仓库或 PR/issue 工作流，但不是这个 skill 的基础要求。

Python 也是可选的。`scripts/render_report.py` 只使用 Python 标准库，主要用于在已有结构化数据时稳定生成 Markdown 报告。即使不用这个脚本，skill 仍然可以在聊天中输出结果，并写入 Markdown 文件。

需要注意的是，GitHub 趋势数据本身有时间窗口和来源差异。不同网站可能使用 weekly calendar、rolling 7 days 或其他统计方式，所以 TrendFollower 的输出会尽量标明数据来源、排序方式和当前限制，不把结果包装成绝对完整或永久准确的排名。

## 项目结构

```text
skills/
  trend-follower/
    SKILL.md
    agents/openai.yaml
    references/source-policy.md
    references/output-format.md
    scripts/render_report.py
```

生成的报告不属于 skill package 本身。`outputs/` 只是 workspace fallback，用来在默认用户级路径不可写时保存报告。

## 本地验证

如果需要检查 skill 文件结构，可以运行本地 validator。这个 validator 可能需要 `PyYAML`：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/trend-follower
```

也可以测试报告 formatter：

```bash
printf '[{"repo":"owner/repo","url":"https://github.com/owner/repo","growth":"+100 stars","purpose":"Example project.","source":"Fixture","source_url":"https://example.com"}]' | python3 skills/trend-follower/scripts/render_report.py --mode 1 --sources "Fixture" --limitations "Fixture data for local testing only."
```
