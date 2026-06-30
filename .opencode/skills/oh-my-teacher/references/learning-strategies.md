# Learning Strategies

Use this file to choose study methods for `/plan`, `/quiz`, `/fix`, `/socratic`, `/feynman`, `/flashcards`, and any request about how to learn efficiently. Pair strategy choice with `references/focus-feedback-iteration.md` so each strategy produces focus, feedback, and a next iteration.

## 策略选择（Strategy Selection）

优先选择让学生主动检索、解释、对比或迁移的策略。除非学生第一次接触某主题，否则避免长篇被动摘要。

| 学习需求 | 策略 | 产出形式 |
|----------|------|----------|
| 记住事实、公式、定义 | **检索练习**（Retrieval practice） | 简答、闪卡、填空 |
| 跨天/周保持记忆 | **间隔复习**（Spaced practice） | SRS 排期和到期复习 |
| 区分相似方法或题型 | **交错练习**（Interleaving） | 混合题组 + "先选方法"提示 |
| 理解为什么成立 | **精细加工**（Elaborative interrogation） | 为什么/什么时候/如果...会怎样 |
| 检查能不能教别人 | **费曼复述**（Feynman technique） | 学生讲解、追问、修复卡 |
| 逐步建立推理 | **苏格拉底追问**（Socratic questioning） | 一次一问、提示阶梯、学生总结 |
| 避免死记硬背 | **具体例子**（Concrete examples） | 正例、反例、边界例 |
| 学习结构/流程/机制 | **双编码**（Dual coding） | 文字 + 图示/表格/状态追踪/流程图 |
| 提升解题监控能力 | **自我解释**（Self-explanation） | 学生解释每步的目的和条件 |
| 阅读前聚焦注意力 | **预测试**（Pretesting） | 先做诊断题再讲解 |
| 跨变式迁移 | **类比对照**（Analogical comparison） | 对比两道题/两个概念/两种解法 |
| 发现"以为会了"的盲区 | **信心校准**（Confidence calibration） | 答前预测把握度，答后对比实际分 |

## 循证默认规则（Evidence-Informed Defaults）

- 学生已接触过某主题 → 先做**检索练习**，不要先重新阅读。
- 每次批改或修复后 → 更新**间隔复习**排期。
- 学生能做基础单主题题 → 加入**交错练习**。
- 学生答得出但说不清为什么 → 用**精细加工**追问。
- 证明/推导/算法/代码追踪/实验步骤 → 要求**自我解释**。
- 需要精确理解时 → 先给**具体例子**，再做类比。
- 流程/系统/空间关系/状态变化 → 用**双编码**配图。
- 学生不知道该关注什么 → 用**预测试**聚焦注意力。
- 高风险或"我肯定会"的主题 → 用**信心校准**暴露盲区。
- 每次策略产生反馈后 → 选一个迭代动作：修复、重做、交错、升级、降优先级或排期。

## 策略详解（Strategy Recipes）

### 检索练习（Retrieval Practice）

先出题再讲解：

1. 一道记忆题：定义、公式、定理条件、语法或实验步骤。
2. 一道理解题：为什么、什么时候、对比或反例。
3. 一道应用题：解题、证明、计算、调试、解读或操作。

批改后更新 SRS。

### 交错练习（Interleaving）

学生已练过至少两个相关主题时使用。

题组结构：

1. 主题 A 的一道题。
2. 主题 B 的一道看起来很像的题。
3. 一道"先选方法再做"的题。
4. 一道混合题，要求学生说明为什么选这个方法。

批改后必须附一句"如何识别这种题型"的总结。

### 精细加工（Elaborative Interrogation）

追问：

- 这个条件为什么重要？
- 去掉这个条件会怎样？
- 能满足这个条件的最简单例子是什么？
- 能推翻它的最简单反例是什么？
- 最容易跟它混淆的相邻概念是什么？

用于苏格拉底模式、口试模拟、证明修复和概念对比。

### 自我解释（Self-Explanation）

用于多步骤解答。要求学生标注每一步：

```markdown
这一步做了什么：
为什么这么做：
用到了什么条件：
可能的陷阱：
```

批改时检查每步的理由是否逻辑成立，不只看最终答案对不对。

### 具体例子（Concrete Examples）

对抽象概念，要求三个例子：

- **正例**：满足定义或方法的例子。
- **反例**：看起来很像但不满足的例子。
- **边界例**：最小的、极端的、退化的或边界情况。

编程题的边界例：空输入、单元素、重复值、最大规模、非法输入（如适用）和 off-by-one。

### 双编码（Dual Coding）

文字配最小必要图示：

- 数学：证明依赖图、数轴、函数草图、条件表。
- CS：状态追踪表、内存图、栈/队列/表、算法流程图。
- 物理/工程：受力图、电路/流程图、单位表。
- 医学/生物/化学：机制链、结构-功能图、对照表。
- 文科/法学/经济：时间线、论证图、案例对比表。

纯聊天环境用 ASCII 或 Markdown 表格。Agent shell 中用 Mermaid、图表、HTML 或可运行 demo。

### 预测试（Pretesting）

阅读或总结章节前，先出 2-3 道低风险题。目标不是打分，是聚焦注意力。

```markdown
## 预测试
1. [问题]
2. [问题]
3. [问题]

答完后我会根据你的错误来决定重点讲什么。
```

### 类比对照（Analogical Comparison）

两个概念容易混淆或学生选错方法时使用。

```markdown
| 对比维度 | 概念/方法 A | 概念/方法 B | 考试识别信号 |
|----------|------------|------------|-------------|
```

然后给一道混合识别题。

### 信心校准（Confidence Calibration）

用于暴露"以为会了"的盲区——感觉准备好了和真正准备好了之间的差距，是考试无声丢分的最大来源。

1. Before revealing the answer or grading, ask the student to rate confidence 1-5 (or %): "答这道题前，先估一个把握度 1-5。"
2. Grade as usual.
3. Compare prediction to outcome and name the calibration zone:

```markdown
| 信心 | 实际 | 校准 |
|---|---|---|
| 5（很有把握） | 6/10 | 过度自信 ⚠ 优先复习 |
| 2（没把握） | 9/10 | 低估自己，可少花时间 |
```

- **Overconfident** (high confidence, low score): flag as a priority weak point even though it "felt" known; route to `/fix` and SRS.
- **Underconfident** (low confidence, high score): reassure and de-prioritize to save time.
- **Well-calibrated**: proceed normally.

Track recurring overconfidence in the snapshot's Weak points so the final-week plan front-loads those topics.

## 禁忌（Anti-Patterns）

- 用户要备考时，不要用长篇摘要替代练习。
- 完全没学过的学生，不要上来就用费曼模式——先讲一遍再让他复述。
- 学生对各子主题还没有基本掌握时，不要上交错练习。
- 不要生成纯装饰性的图示——图必须澄清关系、流程或状态。
- 不要因为答对一道简单题就标记为已掌握——要求变式或迁移成功。
- 多步复习回合不要没有下一步就结束——必须给一个具体迭代目标。
