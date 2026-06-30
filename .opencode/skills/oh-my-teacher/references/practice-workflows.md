# Practice Workflows

用于主动回忆、`/mock`、`/oral`、`/fix`、`/summary` 和练习修复闭环。学习策略选择见 `references/learning-strategies.md`；保持“聚焦 - 反馈 - 迭代”见 `references/focus-feedback-iteration.md`。

## Active Recall

能出题时先出题，再总结。中文用户备考时，默认不要先给长篇知识点摘要。

可用形式：

- 闪卡：正反面、cloze、公式、定义、对比。见 `SKILL.md` Flashcard Export 和 `scripts/export_flashcards.py`。
- 简答抽查。
- 流程步骤填空。
- 证明骨架补全。
- 代码输出预测。
- 实验操作清单回忆。
- 中文背诵课：名词解释、辨析题、论述提纲补全、关键词默写。

每轮主动回忆后，更新相关 SRS 行（见 `references/spaced-repetition.md`），让掌握主题延后复习，薄弱主题更快回炉。

每轮主动回忆必须说明当前 focus topic，收集可见答案信号，并以一个迭代动作结束：repair、repeat、interleave、escalate、de-prioritize 或 schedule。

每个概念分三层：

1. Memory：定义/公式/事实。
2. Understanding：解释原因、条件或对比。
3. Exam application：解题、证明、计算、调试或分析。

当学生已掌握基础时，混入相近主题，不要重复刷同一种套路。使用 `references/learning-strategies.md` 的 interleaving 迫使学生识别方法。

中文 `/quiz` 输出默认：

```markdown
当前重点: [topic]
难度: [基础/变式/综合]
预计用时: [minutes]

题目:
[question]

请先作答。需要提示就说“提示1”。
```

批改后按 `references/question-types.md` 的中文评分结构输出，并给下一题难度调整。

## Mock Exam

生成模考时必须说明：

- 总分和时间。
- 题型分布。
- 是否闭卷/开卷/半开卷/可用资料假设。
- 难度分布。
- 答案和评分 rubric。
- 每题/每部分时间分配建议。

中文 `/mock` 模板：

```markdown
# 模拟卷
- 总分:
- 时间:
- 考试形式假设:
- 做题顺序建议:

## 题目
[按题型和分值列出]

## 答题要求
[是否先隐藏答案；如何提交答案；是否记录用时]
```

学生答完后，按 `question-types.md` 规则批改。

### Triage Training (审题分流训练)

模考不仅练知识，更练临场策略。在生成模考卷后、学生答题前，先进行一轮审题分流训练：

1. **黄金 5 分钟扫卷**：生成模考卷后，先封锁答题。要求学生花 1-2 分钟扫视全卷，回答：
   - 哪道是你能快速拿分的"低垂果实"？
   - 哪道是需要最后做的"时间杀手"？
   - 请排出你的答题顺序。

2. **反馈答题顺序**：对学生排出的顺序给出建议，指出时间陷阱和得分效率。

3. **进入计时答题**：确认顺序后再开始。

```markdown
## 审题分流（Exam Triage）
请先花 1 分钟扫视全卷，然后告诉我：
1. 最有把握的"快拿分"题号：
2. 最可能超时的"时间杀手"题号：
3. 你打算的答题顺序：

我会对你的策略给出建议，然后开始计时。
```

冲刺模式下可跳过 triage，但至少提醒"先做会的、后做难的"原则。

### Pacing and Time Management

模考也是时间分配训练。很多学生不是不会，而是难题耗时过长导致后面丢分。必须显式训练 pacing：

- 先给每题/每部分时间预算，总和等于考试时间，基本按分值比例分配。
- 可行时要求用户记录每题实际用时，或标出超时题。
- 模考复盘中，时间问题和知识错误并列指出：

```markdown
## 节奏复盘
| 题 | 分值 | 预算 | 实际 | 判断 |
|---|---|---|---|---|
| 大题3 | 15 | 18min | 32min | 超时，应在 20min 时战略性跳过 |
```

- 教 triage 规则：先做单位时间得分高的题；每题设硬上限；卡住就标记返回，不要硬耗。
- 机考/OJ 的 pacing 是做题顺序，不是部分分。

## Error Repair

批改或复盘错误时：

1. 找到最小错误知识点。
2. 分类错误：概念、条件、公式、计算、证明缺口、代码边界、实验操作、表达。
3. 给一个微课，不要重讲整章。
4. 如果错误涉及证明、推导、代码追踪或实验操作，要求学生用一句话解释改正后的关键步骤。
5. 生成三类修复：基础题、变式题、综合/混合题。
6. 如果错在“选错方法”，增加一道方法识别题。
7. 更新下一步复习建议。
8. 更新该主题 SRS 行（见 `references/spaced-repetition.md`）；Agent shell 中优先用 `scripts/srs.py update`。

中文 `/fix` 输出模板：

```markdown
## 错因定位
## 3 分钟微课
## 你来复述
## 修复练习
1. 基础:
2. 变式:
3. 综合:
## 下一轮
## 本轮闭环
```

错题修复必须以 `references/focus-feedback-iteration.md` 的 `本轮闭环` 结束：focus = 精确薄弱点，feedback = 答案证据，next round = 一个定向动作。

## Oral Exam Rehearsal

用于 `/oral`、口试、实验 viva、答辩和面试式考核。一次只问一个问题，等用户回答，批改后再决定加深或修复。

开场设置：

- 确认科目、预计时长和已知评分标准。
- 每个主题建立 6-12 个问题阶梯。
- 除非确认支持音频，默认文字口试。

深度阶梯（由浅入深，卡住就停）：

| 层级 | 问法 | 参考时间 |
|------|------|----------|
| 1 | 定义/概念：这是什么？ | 约 30 秒 |
| 2 | 条件/范围：什么时候成立？什么时候不行？ | 约 45 秒 |
| 3 | 举例/反例：给一个正例和一个反例 | 约 45 秒 |
| 4 | 应用：用这个来解决一个问题 | 约 90 秒 |
| 5 | 边界/特殊情况：极端条件下会怎样？ | 约 60 秒 |
| 6 | 对比：跟相似概念有什么区别？ | 约 60 秒 |
| 7 | 辩护：别人说"这个不对"，你怎么反驳？ | 约 60 秒 |

学生卡住时立刻停止追问，修复缺口后再继续。

按准确性、简洁度、结构、信心和课程术语批改每个回答。

教可复用短答模板：

- 定义 -> 关键条件 -> 例子 -> 常见坑。
- 若条件成立 -> 结论；反例说明限制。
- 概念 A vs 概念 B 主要差在某个维度。

中文 `/oral` 默认开场：

```markdown
我会按口试方式一次问一个问题。你回答后，我会给分、指出缺口，再决定追问还是修复。
第 1 题（30 秒）：[question]
```

### Voice and Immersion (Agent Shell)

When the host environment supports audio or TTS tools:

- Generate the examiner's question as audio (TTS) so the student hears the question rather than reading it, simulating real oral-exam pressure.
- If speech-to-text is available, accept the student's spoken answer and transcribe it for grading.
- Always provide a text fallback alongside audio so the student can review what was asked and answered.

In plain chat or RAG notebook, skip audio and use text only.

## Reflect (复盘反思)

`/reflect` 或在 `/summary` 结束时自动触发。用于齐默曼 SRL 循环的自我反思阶段：

```markdown
## 复盘反思（Reflect）
- 本轮目标是什么：[我计划攻克什么]
- 实际完成了什么：[做了什么、正确率如何]
- 最值得修的错误：[一个最高收益错误点]
- 校准差距：预测分 [X] vs 实际分 [Y] → [校准评价]
- 下一轮只做一件事：[一个具体动作]
- 实施意图：[明天 HH:MM，我先做 N 分钟 XXX，再刷 M 道 YYY]
```

反思不是长篇总结，是"一个最值得修的点 + 一个具体下一步"。学生不回答时，AI 从本轮证据推断一句并继续。

## Summary

`/summary` 输出：

- 本轮练过的主题。
- 正确率/表现变化。
- 检索审计：成功检索了什么 / 检索失败了什么 / 下次何时再检索。
- 更新后的薄弱点。
- SRS 更新（如可用）。
- 一个具体下一步。
- focus-feedback-iteration 状态：当前优先重点、最强反馈证据、下一轮目标。

中文模板：

```markdown
## 本轮复盘
- 练习内容:
- 表现变化:
- 新增/修正薄弱点:
- SRS:

## 检索审计（Retrieval Audit）
- ✅ 成功检索: [无提示正确回忆的知识点]
- ❌ 检索失败: [需要提示或答错的知识点]
- 📅 下次检索: [失败项的下次复习日期和建议形式]

## 下一步
[一个马上执行的动作]

## 本轮闭环
重点:
反馈:
下一轮:
```

检索审计帮助学生区分"看过了"和"真的能回忆出来"，是复习效果的核心指标。没有练习数据时省略此节。

保持足够短，能直接粘到学习日志或课程主页。

## Transfer Drill (迁移专练)

`/transfer` 或在 `/quiz` 中指定 `变式/混合/迁移` 时进入迁移专练模式。只练变式题、混合题和迁移题，不练基础题。适用于学生基础已稳、需要突破应用层的场景。

### 触发条件

- 用户运行 `/transfer [topic]`
- 或 adaptive-state 中 topic 的 transfer_level 为 `same` 且 mastery_band >= `ok`（基础已过关，需要升级迁移能力）

### 题目生成规则

1. **变式题**：同一方法，换条件、换数字、换背景。
2. **混合题**：两个相关主题交叉，需要学生判断用哪个方法。
3. **迁移题**：把已学方法应用到新情境（跨章节、跨题型、实际问题）。

```markdown
## 迁移专练
当前主题: [topic]
当前迁移水平: [same / variant / mixed / novel]

### 第 1 题（变式）
[改变条件但方法相同]

### 第 2 题（混合）
[两个主题交叉，先判断方法]

### 第 3 题（迁移）
[新情境下应用同一核心原理]
```

每题批改后更新 adaptive-state 的 `transfer_level`。全部答对 → 升级到下一级。
