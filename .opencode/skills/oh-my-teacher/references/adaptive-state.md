# Lightweight Adaptive State

Use this file when choosing the next review action for `/plan`, `/map`,
`/dashboard`, `/summary`, `/quiz`, `/fix`, reminders, or any workflow that needs
to decide what the student should do next.

This is a pragmatic recommendation layer, not a psychometric model. Do not call
it real IRT, CAT, BKT, DKT, MIRT, or knowledge tracing unless the deployment has
a calibrated item bank, enough response history, and benchmark evidence.

## 主题状态字段（Topic State Fields）

Keep human-facing progress in the Current Course Snapshot. When file persistence
exists, keep machine-readable topic state in `.oh-my-teacher/state.json` under
`adaptive.topics`.

Each topic entry may contain:

```json
{
  "priority": "P0",
  "mastery_band": "weak",
  "scaffold_level": "teach",
  "last_evidence": "quiz 2/5 on 2026-06-13",
  "evidence_count": 3,
  "prerequisites": ["limits-definition"],
  "blocked_by": ["limits-definition"],
  "exam_scope_weight": 30,
  "past_paper_frequency": 2,
  "teacher_emphasis_strength": "high",
  "confidence_gap": 2.5,
  "hint_dependency": false,
  "transfer_level": "same",
  "exam_readiness": false,
  "last_clean_retrieval": null,
  "q_matrix_weak_attribute": "边界条件"
}
```

Field meanings:

- `priority`: `P0`, `P1`, `P2`, or `unknown`; derived from exam-scope weight,
  past-paper frequency, and teacher-emphasis strength.
- `mastery_band`: `weak`, `unstable`, `ok`, or `strong`; derived from quiz,
  mock, grade, oral, SRS, wrong-note, or confidence-calibration evidence.
- `scaffold_level`: `teach`, `guide`, `prompt`, or `test`; controls how much help
  the AI gives before asking the student to perform.
- `last_evidence`: the most recent visible signal that justified the state.
- `evidence_count`: total number of graded attempts on this topic.
- `prerequisites`: small list of required earlier topics.
- `blocked_by`: prerequisites currently blocking progress on this topic.
- `exam_scope_weight`: numeric percentage or point share when known.
- `past_paper_frequency`: count of recent papers where the topic appeared.
- `teacher_emphasis_strength`: `high`, `medium`, `low`, or `unknown`.
- `confidence_gap`: difference between student's predicted confidence and actual
  performance (positive = overconfident). Overconfident topics (gap >= 2) are
  priority weak points that need front-loading in the plan.
- `hint_dependency`: `true` when the student consistently needs hints to answer
  correctly on this topic. Prevents false mastery — a hint-dependent correct
  answer is not exam-ready.
- `transfer_level`: `same`, `variant`, `mixed`, or `novel`; tracks the highest
  difficulty variant the student has successfully completed without help.
- `exam_readiness`: `true` only when the student can answer under exam-like
  constraints (timed, no hints, rubric-scored). A topic can be `ok` mastery
  but not exam-ready if all successes were untimed or hint-assisted.
- `last_clean_retrieval`: ISO date of the last time the student answered
  correctly without any hints or scaffolding. `null` if never.
- `q_matrix_weak_attribute`: the weakest cognitive attribute from the most recent
  Q-matrix diagnosis (e.g. "边界条件", "概念前提", "推导计算"). Used to select
  the right repair strategy.

## 掌握度更新规则（Mastery Band Updates）

仅根据可见证据判定：

- `weak`: score <= 2/5, repeated lost points, high-confidence miss, SRS leech, or
  cannot explain the prerequisite.
- `unstable`: score 3/5, mixed performance, correct answer with missing
  condition, or needs heavy hints.
- `ok`: score 4/5, mostly correct with one small repair.
- `strong`: score 5/5 or repeated clean answers under exam-like constraints.

证据缺失时保持 unknown，不要猜测。

## 支架消退（Scaffolding Fading）

使用共享的四级支架：`teach -> guide -> prompt -> test`（讲解 → 引导 → 提示 → 测试）。

| Level | Use when | AI behavior |
|---|---|---|
| `teach` | new topic, score <= 2, prerequisite missing | explain compactly, show one worked step, then ask a recall question |
| `guide` | score 3, stuck after first attempt, unstable concept | ask targeted questions, give hint ladder, leave key blanks |
| `prompt` | score 4 or two improving attempts | ask the student to choose method, give minimal cues only |
| `test` | score 5 or repeated clean performance | exam-style question first, feedback after answer |

Move one level toward `test` after strong evidence. Move one level back toward
`teach` after a miss, leech warning, or prerequisite block. Do not keep giving
full explanations once the student can perform; transfer responsibility.

## 确定性推荐评分（Deterministic Recommendation Score）

当多个下一步动作可选时，用以下轻量评分排序主题：

```text
score =
  priority_score
  + exam_scope_score
  + past_paper_score
  + teacher_emphasis_score
  + weakness_score
  + srs_due_score
  + prerequisite_block_score
  + urgency_score
```

Default weights:

| Signal | Score rule |
|---|---|
| Priority | P0 +40, P1 +25, P2 +10, unknown +0 |
| Exam-scope weight | numeric percent or points, capped at +25 |
| Past-paper frequency | +6 per appearance, capped at +18 |
| Teacher emphasis | high +18, medium +10, low +3, unknown +0 |
| Mastery band | weak +30, unstable +18, ok +5, strong -20 |
| SRS due | due today +12; overdue adds up to +10 more |
| Prerequisite blocking | +20 when this topic blocks a P0/P1 topic |
| Urgency | days left <= 3: +10 to weak P0/P1 topics |

Tie-breakers: P0 before P1 before P2, weaker mastery first, SRS due first, then
most recent evidence.

推荐动作：

- **弱 + 有阻塞**：先 `/fix` 前置概念。
- **弱 + 无阻塞**：`/fix` 或 `/quiz` 最小失分点。
- **不稳定**：`/quiz` 一道相近变式题，然后批改。
- **尚可**：交错一次或安排 SRS。
- **强**：降优先级做快速回顾，除非是 P0 背诵项。

## Cascade Failure Traceback (级联失效追溯)

When a student repeatedly fails on a downstream topic (mastery_band stays `weak`
after 3+ attempts, or SRS lapses >= 3), do not just reschedule the same topic.
Instead, check whether the failure is caused by a prerequisite gap:

1. Look up the topic's `prerequisites` list.
2. For each prerequisite, check its `mastery_band` and `last_clean_retrieval`.
3. If any prerequisite is `weak`/`unstable` or has never had a clean retrieval,
   the downstream failure is likely a cascade.
4. Pause the downstream topic and route to `/fix` on the weakest prerequisite first.

Output a cascade warning when detected:

```markdown
⚠️ 级联失效警告：[下游主题] 连续失败，疑似上游前置知识缺口。
- 可疑前置概念：[prerequisite A]（mastery: weak, 从未无提示答对）
- 建议：先修复 [prerequisite A]，再回到 [下游主题]。
```

This prevents the student from repeatedly drilling a topic they structurally
cannot solve because the foundation is missing. In cram mode, if the
prerequisite repair would take too long, consider teaching a "保底模板" for
the downstream topic instead.

## 考试就绪度评估（Exam Readiness Assessment）

一个主题只有同时满足以下所有条件才算"考试就绪"：

- `mastery_band` is `ok` or `strong`
- `hint_dependency` is `false`
- `transfer_level` is at least `variant`
- `last_clean_retrieval` is not null and within the SRS interval
- `confidence_gap` is between -1 and +1 (well-calibrated)

For `/dashboard` and `/readiness`, compute an aggregate readiness score:

```markdown
## 考试就绪度（Exam Readiness）
- P0 考点覆盖率：[exam-ready P0 topics / total P0 topics]%
- 限时正确率：[timed correct / timed total]%
- 高信心错题数：[overconfident weak points] ⚠
- 提示依赖考点：[hint-dependent topics] ⚠
- 最大风险：[top 2 risks with reasons]
- 最高收益动作：[one action with expected point gain]
```

This replaces naive "复习进度 X%" with multi-dimensional readiness that
reflects actual exam performance probability.

## 输出契约（Output Contract）

在仪表盘、计划、复盘和推送中，输出紧凑的下一步推荐表：

```markdown
## 下一步推荐
| 排序 | 主题 | 为什么现在做 | 建议动作 |
|------|------|-------------|----------|
| 1 | [主题] | [P0 + 弱点证据 + SRS 到期 / 前置阻塞] | [/fix 或 /quiz 具体动作] |
```

然后以 `references/focus-feedback-iteration.md` 的闭环尾注结束。

## Script Support

In agent shells, prefer:

```bash
python scripts/recommend_next.py --today YYYY-MM-DD
```

Use `scripts/snapshot.py state-merge` to update machine-readable adaptive fields
without changing the human-facing Markdown snapshot. If scripts are unavailable,
apply the same rules manually and emit the recommendation table inline.
