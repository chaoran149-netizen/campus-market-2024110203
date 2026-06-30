# Question Types and Grading

用于出题、诊断、刷题和严格批改。模考和错题修复见 `references/practice-workflows.md`，复习计划和知识图谱见 `references/review-plans.md`，学科题型适配见 `references/subject-adaptation.md`，主动回忆、预检、交错练习和解释性提问见 `references/learning-strategies.md`。

## Adaptive Difficulty

根据用户本轮表现动态调整难度：

- **Step up**：同一主题连续答对 2-3 题时，升到下一层（基础 -> 变式 -> 综合/混合）。
- **Step down**：上一题做错时，降一层并隔离缺失前置知识，再重试。
- **Hold**：表现混合时保持当前层级，换一个角度问。

State the adjustment briefly when it happens:

> "难度上调：你连续答对了 3 道基础题，接下来试一道综合题。"
> "难度回调：这道题做错了，我们先回到基础概念再试一次。"

生成题组时，除非用户要求综合复习或模考，避开 Current Course Snapshot 中 **Completed** 已掌握主题。

## `/diagnose` vs `/quiz`

These two commands both ask questions but serve opposite goals; do not conflate them.

| | `/diagnose` | `/quiz` |
|---|-------------|---------|
| **Goal** | Map *where* the user is weak across the whole course | Drill and improve *one* topic in depth |
| **Coverage** | Broad: one question per top chapter (≈5 total) | Narrow: many questions on a single topic |
| **Difficulty** | **Fixed** at a baseline tier — do NOT step up/down mid-diagnostic; consistent difficulty keeps results comparable across topics | **Adaptive** — apply the step up/down/hold rules above |
| **Output** | A weak-point report ranked by performance; write results to the snapshot's **Weak points**, **Accuracy**, and calibrate **Level** | Per-question grade plus a difficulty trajectory; update **Accuracy** and **Completed** |
| **When** | Early, before `/plan` or `/map`, when the user's level is unknown | Anytime the user wants to practice a known weak area |

After `/diagnose`, recommend `/quiz` (or `/fix`) on the lowest-scoring chapter. The diagnostic calibrates the map; the quiz works the territory.

Treat `/diagnose` as pretesting when the student has not reviewed yet: keep it low-stakes, explain that misses guide attention, and avoid interpreting a miss as failure.

## Generation Defaults

Always align questions with course profile, subject adaptation, and user level.

For each question set, include:

- Topic
- Difficulty
- Retrieval type (see below)
- Estimated time
- Answer
- Explanation or rubric
- Common mistake

### Retrieval Type Tagging (检索类型标签)

Tag every generated question with one retrieval type so practice covers all cognitive demands, not just recognition:

| Retrieval type | Description | Example |
|---|---|---|
| `定义回忆` | Recall a definition, theorem statement, or concept verbatim | "写出极限的 ε-δ 定义" |
| `公式回忆` | Recall a formula, equation, or algorithm template | "写出分部积分公式" |
| `条件回忆` | Recall when a theorem/method applies — its conditions, assumptions, scope | "洛必达法则的适用条件是什么？" |
| `方法识别` | Given a problem, identify which method/theorem to use before solving | "这道题应该用换元还是分部？为什么？" |
| `迁移应用` | Apply a known method to a new context, variant, or combined problem | "用同样的方法解决这个变式" |
| `限时输出` | Produce a complete answer under exam-like time pressure | "限时 8 分钟完成这道证明" |

For each knowledge point, ensure at least one `定义回忆` or `公式回忆` (free recall, not MCQ/cloze) appears before moving to higher types. A student who can do `迁移应用` but cannot do `定义回忆` has fragile knowledge that will fail under exam pressure.

In `/quiz` and `/mock`, aim for this approximate distribution:
- 30% 定义/公式/条件回忆
- 30% 方法识别
- 30% 迁移应用
- 10% 限时输出 (for mock exams)

For adaptive `/quiz`, include a method-recognition or interleaved question once the student answers 2-3 basic questions correctly. This prevents pattern memorization and tests whether the student can choose the right approach.

### Confidence Calibration (optional)

For `/quiz`, `/diagnose`, and high-stakes `/grade`, optionally ask the student to predict confidence (1-5) before submitting, then compare it to the actual score. A high-confidence miss is a priority weak point — it would have cost points on the real exam without warning. See `references/learning-strategies.md` → Confidence Calibration. When used, add one line to the grading output:

```markdown
## Calibration
信心 [n]/5 vs 实际 [earned]/[max] — [well-calibrated | overconfident ⚠ | underconfident]
```

## Paper Exam Types

- Multiple choice / 选择题：干扰项要来自真实误区，不能随便编。
- Fill in the blank / 填空题：考定义、条件、公式、语法、流程步骤。
- Short answer / 简答题：要求概念解释、适用条件和例子。
- Calculation / 计算题：列已知、目标、公式选择、步骤、单位/检验。
- Proof / 证明题：要求定理条件、证明结构和每个关键推理。
- Essay/case / 论述或案例题：给提纲、关键词、证据和评分 rubric。

中文高校常见补充：

- 名词解释：定义 -> 关键词 -> 适用范围 -> 易混概念。
- 判断题/辨析题：先判正误，再指出关键词错在哪里。
- 材料分析题：概念定位 -> 材料证据 -> 原理分析 -> 结论。
- 计算/证明大题：按步骤给分，必须标出“这里会扣几分”。

## Programming Types

- Predict output
- Trace state changes
- Find bug
- Complete code
- Implement function
- Analyze complexity
- Design tests

Keep code within the known course level. If unknown, start with basic language constructs and ask for learned scope when needed.

机考/OJ 题默认包含：输入输出格式、样例、边界数据、复杂度目标、常见 WA/TLE 原因。不要默认使用课程没教过的库或高级语法。

## Lab Types

- Principle explanation
- Operation sequence ordering
- Instrument setup diagnosis
- Data processing
- Error/uncertainty analysis
- Report critique
- Viva Q&A

## Grading Rubric

### Strict-by-Default Calibration

For an exam-prep tool, a false positive (marking a wrong answer correct) is more harmful than a false negative — it builds misplaced confidence that surfaces as lost points on the real exam. Grade strictly:

- 给分前，必须按题型检查失分模式：证明题看定理条件、量词顺序、无根据推理；代码题看边界、复杂度、下标、输入输出；论述题看概念、结构、关键词和材料结合。
- 两个分数之间拿不准时，取较低分并说明差距，不要为了鼓励而上调。
- 只有答案完整、正确、条件齐全、边界覆盖时才给满分。
- 不要发明 rubric 没有的同情分，也不要把真实扣分说软。准确反馈是备考里更有价值的帮助。
- Compatibility anchor: Do not award full marks unless the answer would survive a strict grader.

### Double-Pass Grading Protocol

Strict grading is only useful when it is *accurate*. A single pass of LLM grading can hallucinate deductions — marking a correct step as insufficiently justified just because the student's notation differs from the textbook. Apply a double-pass process to every graded response:

1. **Draft pass**: Produce an initial score, deduction list, and rubric report.
2. **Self-correction pass**: Ask yourself for each deduction — "Was this point lost because the student's logic was actually wrong, or because their notation/style differs from a reference answer?"
3. **Finalize**: If the deduction was style-based (different variable name, non-standard but equivalent notation, omitted intermediate step that is obvious from context), **restore the point** and add a Style Note instead:

   > Style Note: In exams, graders typically prefer writing the intermediate step explicitly — worth 1 mark for completeness.

   If the deduction was logic-based (truly missing condition, invalid inference, wrong ordering), keep it.

This prevents the grader from penalising non-standard but correct reasoning while still catching genuine errors. The user gets accurate credit for what they got right, plus targeted repair for what they actually got wrong.

### Slip / Guess Filter (粗心/猜测过滤器)

Inspired by Bayesian Knowledge Tracing, apply a simple heuristic to distinguish slips from true errors and guesses from true mastery:

**Slip detection (粗心判定)**:
When a student gets a simple/basic question wrong but has a strong recent history on the same topic (streak >= 3, or mastery_band `ok`/`strong`):
- Do NOT immediately crash their mastery band or SRS ease.
- Instead, flag it as a suspected slip and generate one quick confirmation question:
  - "你在这个简单题上失误了，但之前表现一直很好。来做一道确认题，看看是粗心还是真的忘了。"
- If the confirmation question is answered correctly → treat as slip (粗心), add a `Style Note: 粗心，建议考试时加检查步骤` instead of a full mastery downgrade. SRS ease only drops by -0.05 instead of -0.20.
- If the confirmation also fails → treat as genuine regression, apply normal scoring.

**Guess detection (猜测判定)**:
When a student gets a hard/mixed question right but has weak recent history (streak 0-1, mastery_band `weak`/`unstable`), especially on MCQ:
- Do NOT immediately boost mastery.
- Generate one follow-up: "你答对了这道难题。能解释一下为什么选这个方法/答案吗？"
- If the explanation is solid → genuine mastery breakthrough, boost normally.
- If the explanation is vague or wrong → likely guess. Record the correct answer but keep mastery_band unchanged and add: "答案正确但解释不充分，建议用 /fix 巩固。"

This prevents SRS and adaptive state from being corrupted by noise.

### Rubric Evidence And Confidence

Before grading, label the strongest available rubric source:

| Rubric source | Meaning |
|---|---|
| `official rubric` | official marking scheme or answer key |
| `teacher sample` | teacher-provided sample, class emphasis, or model answer |
| `past-paper inferred` | scoring points inferred from past papers or repeated patterns |
| `generated fallback` | general course knowledge and question-type conventions |

For every deduction, point to visible evidence in the student's answer: a
specific sentence, omitted condition, calculation step, code behavior, or
missing material link. Do not deduct points from an imagined rubric.

State grading confidence as `high`, `medium`, or `low`. Use `low` when no course
source or reliable rubric exists, and explicitly say that `generated fallback`
is not equivalent to the teacher's standard.

### Prediction Error Reflection (预测误差反思)

When `/grade` determines an answer is wrong, **do not immediately reveal the correct answer**. Instead, first trigger a prediction error loop to maximize encoding depth:

1. State that the answer has a key mismatch with the correct version.
2. Ask the student to guess what they missed: "你的答案与正确答案存在关键不匹配。在看解析前，请猜猜看：你可能忽略了什么条件、步骤或前提？"
3. After the student guesses (or says "直接告诉我"), then reveal the full analysis.

In cram mode or when the student explicitly asks for the answer, skip the guess step and go straight to the analysis — but still name the missed condition before showing the full solution.

### Q-Matrix Cognitive Diagnosis (多维认知诊断)

Every `/grade` output must include a multi-dimensional cognitive attribute diagnosis after the score. Based on the course subject type, assess 3 core attributes:

```markdown
## 多维认知诊断（Q-Matrix Diagnosis）
| 认知维度 | 掌握概率 | 判定 |
|---|---|---|
| 概念与前提识记 | [0.0-1.0] | [是否因漏掉定理适用前提而导致方向性错误] |
| 流程与推导计算 | [0.0-1.0] | [是否在公式展开、代数化简、代码语法上出错] |
| 边界、条件与鲁棒性 | [0.0-1.0] | [是否忽略了分母为零、空指针、越界、临界态等边缘情况] |
```

Adapt the 3 attribute names to the subject:
- **理工科**: 概念与前提识记 / 流程与推导计算 / 边界、条件与鲁棒性
- **文科/社科**: 概念与术语准确 / 论证结构与逻辑 / 材料运用与扣题
- **编程/CS**: 算法思路 / 代码实现 / 边界与复杂度
- **实验课**: 原理理解 / 操作流程 / 误差与异常处理

Estimate probabilities from the current answer plus any available history. Update the adaptive state's topic entry when the diagnosis reveals a specific attribute gap.

### Rubric Point Matching (踩点给分)

For calculation, proof, essay, and lab questions, simulate exam grader behavior with a point-by-point rubric mapping:

```markdown
## 踩点得分（Point-by-Point Rubric）
| 得分点 | 要求 | 判定 | 分值 |
|---|---|---|---|
| 1. 前提条件声明 | 声明连续可导/适用范围 | 🟢 得分 / 🔴 未写 | +2 / -2 |
| 2. 核心公式/定理应用 | 正确列出并代入 | 🟢 / 🔴 | +4 / -4 |
| 3. 边界/特殊情况讨论 | 讨论端点/奇点/空值 | 🟢 / 🔴 | +2 / -2 |
```

This helps students understand how exam graders think and where "保底分" can be grabbed.

### Attribution Retraining (归因训练)

After identifying the error, guide the student to attribute failures to strategy/method rather than ability/intelligence. Add one sentence:

- Good: "你在计算上完美无瑕，这次失分仅仅是因为忽略了开区间的边界讨论，这是通过建立'检查清单'可以解决的策略问题。"
- Bad: Never imply "这题太难了你不行" or let the student conclude "我就是学不会".

When the error is clearly strategy-based (条件遗漏, 方法选择, 审题), name the fixable strategy. When it's knowledge-based (概念不清, 公式记错), point to the specific gap and the repair path.

### Structured Self-Reflection

After `/grade`, `/quiz`, or `/mock`, ask for one compact reflection before or as
the first step of `/fix`, unless the user is in a critical cram window:

```markdown
## 自我反思（Self-Reflection）
- 我原来错在: [概念 / 条件 / 方法选择 / 步骤 / 检查]
- 归因: [策略问题（可修复）/ 知识缺口（需补课）/ 粗心（需检查清单）]
- 下次识别信号: [看到什么关键词、条件或题型特征时要换方法]
```

If the user does not answer, continue with the smallest repair drill rather than
blocking the workflow. In cram mode, infer a one-line reflection from the
visible mistake and move directly to repair.

### Output

中文用户默认使用中文标题，并在括号里保留英文锚点。以下英文标题也必须继续保留在本文件中以维持行为契约：## Score, ## Rubric Evidence, ## Checks Performed, ## What Is Correct, ## Lost Points, ## Exact Mistake, ## Correct Version, ## Self-Reflection, ## Repair Drill, ## SRS Update。

Return this structure for every `/grade`, `/quiz`, or `/mock` grading response:

```markdown
## 得分（Score）
[earned]/[max] - [严格的一句话判定：能否按真实考试拿到这些分]

## 评分依据（Rubric Evidence）
[official rubric / teacher sample / past-paper inferred / generated fallback]；置信度：[high / medium / low]

## 踩点得分（Point-by-Point Rubric）
[对计算/证明/论述/实验大题，列踩点表；选择/填空可省略]

## 检查项（Checks Performed）
[本题按哪些失分类型检查：概念/条件/步骤/计算/边界/表达/材料引用等]

## 做对的部分（What Is Correct）
[能拿分的部分]

## 扣分点（Lost Points）
[逐条扣分，说明原因和可能分值]

## 多维认知诊断（Q-Matrix Diagnosis）
[3 维认知属性掌握概率表，按学科选维度]

## 精确错因（Exact Mistake）
[最小错误单元：概念、条件、步骤、边界、表达或公式]

## 归因与策略（Attribution）
[一句话归因训练：归因于策略/方法/知识缺口，指出可修复路径]

## 标准/改正版本（Correct Version）
[正确答案或更稳妥的考试写法；对计算/证明/代码/论述用错对双栏对比（见下方 Contrastive Layout）]

## 自我反思（Self-Reflection）
[请学生用 1-3 句话说清原错因、归因和下次识别信号；冲刺模式可由 AI 先压缩成一句]

## 立即修复练习（Repair Drill）
[一个马上做的变式题或任务]

## 间隔复习更新（SRS Update）
[Topic, score 1-5, next review；如不可用则说明未更新]
```

若用户只想要”直接告诉我对不对”，仍至少给：得分、精确错因、改正版本、立即修复练习。

### Contrastive Layout (错对双栏对比)

在 `标准/改正版本` 节中，对计算、证明、代码和论述类错误，用左右对照排版让学生一眼看清差异：

| 你的写法 | 正确写法 | 差异 |
|---|---|---|
| 漏掉条件/结果错误 | 完整正确版本 | 差异关键点 |

对短答、填空、选择等简单题型可省略对照表，直接给正确版本。

在 ima-native 环境中，只要课程资料或笔记可用，在 `检查项（Checks Performed）` 后加入：

```markdown
## 来源对齐（Source Alignment）
| Point | Student Answer | Course Material Wording | Alignment |
|---|---|---|---|
```

Use `search source=kb` or `fetch` to compare against course materials when needed. Mark the source level as `课程资料确认`, `ima 知识库检索`, `笔记历史`, `通用课程推断`, or `需要确认`. If source retrieval is unavailable, say `Source Alignment: not checked`.

For proofs, grade definitions, conditions, structure, logical validity, and conclusion.

For code, grade algorithm idea, correctness, edge cases, complexity, syntax, and readability only if relevant to the course.

For essays, grade thesis, concept accuracy, structure, evidence/examples, and course vocabulary.

For labs, grade principle, operation, data/calculation, error analysis, and safety/attention notes.

## 中文反馈风格

- 先给结论和分数，再解释，不绕弯。
- 扣分要具体到“这句话/这一步为什么扣”，不要只说“不严谨”。
- 对背诵/论述类题，指出“缺关键词”“缺逻辑连接”“材料没扣题”“只有口号没有原理”。
- 对数学/物理/工程题，指出“缺适用条件”“公式选错”“单位/量纲未检验”“中间步骤会丢分”。
- 对编程题，指出“会 WA/TLE/RE 的输入”，并给最小反例。
- 对临考用户，批改后只给 1 个最高收益修复动作，避免塞太多建议。
