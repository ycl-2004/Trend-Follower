# TrendFollower：我把筛 GitHub 项目的过程做成了一个 Codex Skill

最近刷到很多 AI 工具推荐。

“这个 GitHub 项目爆了。”

“本周最强 AI agent。”

“程序员一定要看的开源工具。”

一开始我也会点进去看，但看多之后发现，真正耗时间的不是“有没有项目可以看”，而是“哪些项目值得继续看”。

很多时候，我会先看到一个推荐，再点进 GitHub，看 README、stars、demo，甚至再丢给 AI 总结一轮。最后才发现，这个项目跟我当下其实没太大关系。

所以我做了一个小 Codex Skill，叫 **TrendFollower**。

它的目标很简单：帮我先扫一遍过去一周 GitHub 上增长比较快的开源项目，再用简单的话说明它们是做什么的。

它不会替我决定哪个项目一定值得用，但可以先帮我完成第一轮筛选。这样我不用每次都从一堆视频、帖子和 README 里重新找重点。

现在它可以这样调用：

```txt
/trendfollower
/trendfollower 1 agent
/trendfollower 2 20 coding tools
```

mode `1` 看一周新增 stars，mode `2` 看 7 天增长百分比。后面也可以加 topic，比如 agent、coding tools、automation。

做这个项目之后，我更明显地感觉到：AI 编程不是一句话让模型直接生成一个完整项目，而是先把一个真实的小问题拆清楚，再把反复出现的动作整理成可以复用的 workflow。

TrendFollower 本身不复杂，但它让我确认了一件事：好的 AI workflow 不一定要很大，它只要能减少一次又一次的重复筛选，就已经有价值了。

## 平台宣发版本

### 小红书：经验分享型

定位：

```txt
项目经验复盘 / AI 工具使用心得
```

标题：

```txt
不是让 AI 直接写代码，而是让 AI 帮我拆项目
```

正文文案：

```txt
最近刷到很多 AI 工具推荐。

“这个 GitHub 项目爆了。”  
“本周最强 AI agent。”  
“程序员一定要看的开源工具。”

一开始我也会点进去看，但看多之后发现，真正浪费时间的不是“看项目”，而是“筛项目”。

很多时候流程都是这样：

看到一个推荐。  
点进 GitHub。  
读 README。  
看 stars 和 demo。  
再丢给 AI 总结一轮。  
最后发现：这个项目其实不是我需要的。

所以我做了一个小 Codex Skill，叫 **TrendFollower**。

它会帮我整理过去一周 GitHub 上增长最快的开源项目，并用比较简单的话说明：

- 项目叫什么；
- 链接在哪里；
- 最近涨了多少；
- 它到底是做什么的。

调用方式也很简单：

/trendfollower 1

看本周新增 stars 最多的项目。

/trendfollower 2

看 7 天增长百分比最快的项目。

我做它不是为了再造一个“工具榜单”，而是想把“筛 GitHub 项目”这个重复动作变成一个固定 workflow。

它不会替我决定哪个项目一定值得用，但它可以先帮我做第一轮筛选。这样我不用每次都从一堆视频、帖子和 README 里重新找重点。

少刷一点内容。  
少烧一点 token。  
先看 overview，再决定要不要深入研究。

这可能就是我现在最需要的 AI 工作流：不是更复杂，而是更省心。
```

标签：

```txt
#AI工具 #项目复盘 #Codex #GitHub #开源项目 #AI学习 #学生项目 #效率工具
```

### X：Build In Public Thread

Thread 文案：

```txt
1/ I built a small Codex skill: TrendFollower.

The goal is simple:
find fast-growing GitHub repos from the past week, then explain what they actually do and whether suitable to use in your OWN case.

2/ The problem I wanted to solve was not “there are no project recommendations.”

It was the opposite.

There are too many: GitHub Trending, X posts, newsletters, videos, and random tool lists.

The real cost is filtering.

3/ My usual flow was messy:

- see a repo recommendation
- open GitHub
- read the README
- check stars / demo / use case
- ask AI to summarize it
- then realize it was not relevant

That repeated workflow felt worth turning into a skill.

4/ The workflow became:

Find sources → filter repos → rank by growth → explain each project clearly.

It is not trying to replace judgment.
It just helps me get to the judgment stage faster.

5/ Current usage looks like:

/trendfollower
/trendfollower 1 agent
/trendfollower 2 20 coding tools

Mode 1 ranks by weekly stars gained.
Mode 2 ranks by 7-day percentage growth.

6/ The biggest limitation right now is runtime.

There is no backend, cache, or keyword dictionary yet, so broad topics still require checking repos and README files one by one.

Soft limit: ~3 min
Hard limit: ~5 min

7/ The main lesson:

AI is not just useful for writing code.
It is useful for turning a vague recurring workflow into something structured, repeatable, and executable.
```

### 抖音：口播

视频：

```txt
我用 AI 做了一个 GitHub 趋势追踪小工具
```

60-90 秒口播：

```txt
你有没有发现，现在 GitHub 上每天都有很多新的 AI 工具和开源项目。

但真正麻烦的不是找不到项目，而是你要一个个点进去看 README、看 stars、看 demo，最后才知道它到底值不值得研究。

现在一个项目解决你的问题 TrendFollower

它不是一个完整平台 只是一个简易Codex skill

我想做的事情很简单：把“找最近增长比较快的 GitHub 项目”这个重复流程，变成一个可以调用的 AI workflow。

通过简易输入：

/trendfollower 1 agent

它就会围绕 agent 这个方向，去找最近增长比较快的 GitHub 项目，然后用简单的话告诉我这些项目分别是做什么的以及适不适合现在使用。

这个项目本身不复杂，但我觉得它比较有意思的是：AI 不只是帮我写代码，它也帮我把一个模糊想法拆成了可以执行的 workflow。
```

### Bilibili：项目复盘

视频标题：

```txt
我用 AI 做了一个 GitHub 趋势追踪 Skill，从选题到落地复盘
```

视频简介：

```txt
这期视频复盘一个小项目 TrendFollower。

它是一个 Codex skill，用来发现过去一周 GitHub 上增长比较快的开源项目，并用简洁语言解释这些项目是做什么的。

这个项目本身不复杂，我更想讲的是它从 0 到 1 的过程：我为什么选这个题，怎么用 AI 做前期调研，怎么把想法拆成 workflow，最后怎么落地成一个可调用的 skill。
```

结构：

```txt
00:00 我为什么做这个项目
01:00 问题不是找不到项目，而是筛选成本太高
02:00 我用了哪些 AI 工具，各自负责什么
03:00 TrendFollower 的 workflow 拆解
04:00 当前版本怎么调用
05:00 当前限制：执行时间偏长
06:00 下一步：keyword 字典、缓存、运行路径优化
07:00 这次项目给我的启发
```

### 微信：长文型

微信更适合完整文章，重点是逻辑、可信度和沉淀价值。这里可以接近当前 `Post.md` 的母稿，但开头要更稳，最好声明这是个人项目复盘，不是自动化批量生成内容。

标题备选：

```txt
TrendFollower：我如何用 AI 把一个信息筛选问题整理成 Workflow
```

正文开头：

```txt
所以这次项目的重点不是功能本身，而是一个想法如何从观察、调研、结构化拆解，最后变成一个可以执行的 AI workflow
```

正文结构：

```txt
1. 我为什么选择这个选题
2. 我观察到的问题：信息很多，但筛选成本很高
3. 我如何使用 Grok、Gemini、GPT 和 Codex
4. 我怎么把问题拆成 Find、Filter、Rank、Explain
5. 当前版本实现了什么
6. 当前限制：执行时间偏长
7. 下一步：keyword 字典、缓存和执行路径优化
8. 这次实践给我的启发
```

## 平台规则

- 小红书：偏真实分享、友好互动 适合经验复盘和可收藏内容
- X：信息简洁 连续短文
- 抖音：内容需要真实、有依据，短视频要重视前几秒和完播。
- Bilibili：基于真实信息表达观点
- 微信：公众号内容更适合完整
