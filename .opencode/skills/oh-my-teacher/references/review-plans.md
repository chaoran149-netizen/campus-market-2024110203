# Review Plans and Study Maps

用于 `/plan`、`/map`、`/cram`、`/last-page`、`/dashboard`、多课程排期、考前一页纸和进度热力图。学习策略选择见 `references/learning-strategies.md`；复习闭环见 `references/focus-feedback-iteration.md`；下一步排序见 `references/adaptive-state.md`；显式每日/每周提醒或知识归纳见 `references/opt-in-reminders.md`。

## Study Map

存在课程知识库时（见 `references/course-wiki.md`），优先从 wiki 的章节 MOC / `INDEX.md` 渲染知识树，而不是从零重建；`/map` 与 wiki 共享同一套页面与优先级。

Produce:

- 课程画像假设：考试形式、剩余时间、目标分、资料置信度。
- 章节/知识树：按教材章节和老师课件顺序对齐。
- 优先级标签：必会、高频、难点、快速扫过、低优先级。
- 当资料包含考试范围、往年题或老师强调时，必须给 "Most Worth Studying Chapters" 表。按 exam-scope weight + past-paper frequency + teacher-emphasis strength 排 P0/P1/P2；缺证据写 unknown。
- 考试动作：背、理解、推导、计算、写代码、画图、操作、套模板。
- 可能题型和常见坑。
- 下一组练习。
- Current Course Snapshot 有 Accuracy 或 SRS 数据时，加入进度热力图。
- 当前复习闭环：重点、反馈证据、下一轮目标。

如果有往年题，从重复概念、题型、分值和出现年份估算权重。避免说“必考”，改说“高频/证据强/需要确认”。

当多个主题都值得复习时，按 `references/adaptive-state.md` 的确定性推荐分数排序，综合章节优先级、考试范围、真题频率、老师强调、薄弱证据、SRS 到期和前置知识阻塞。不要只按学生主观感受或最近对话顺序排计划。

中文输出建议结构：

```markdown
## 课程假设
## 知识树与章节地图
## Most Worth Studying Chapters
## 掌握度热力图
## 高频题型与常见坑
## 下一组练习
## 本轮闭环
```

## Progress Heat Map

对 `/map` 和 `/plan`，只要有掌握度数据，就给每章/主题一个紧凑 ASCII 进度条：

```text
Topic                    Mastery
Limits and continuity    [########--] 80%  (8/10 accuracy, SRS streak 3+)
Differentiation          [######----] 60%  (6/10 accuracy)
Integration              [##--------] 20%  (2/10 accuracy)
Series                   [----------]  0%  (not yet practiced)
```

Compute mastery as:

1. If Accuracy has a score for the topic: `pct = accuracy_score * 10`, capped at 100.
2. If no Accuracy data but SRS has entries: `pct = topics_at_streak_3_plus / total_topics_in_chapter * 100`.
3. If neither exists: `pct = 0`.

Place the heat map after the knowledge tree and before common traps.

## Review Plan

使用剩余天数和每天可用时间。计划必须现实，不要把 10 小时任务塞进 2 小时。

必须包含：

- 每日底线任务：为了目标分必须完成的部分。
- 可选加分任务：冲更高分时再做。
- 每天必须有主动回忆，不允许只安排“看书/看 PPT”。
- 每个学习块标注策略：retrieval、spaced review、interleaving、self-explanation、Socratic、Feynman、dual coding、mock。
- 练习后必须安排错题修复。
- 考前安排一次模考或微型限时套题。
- 最后 30 分钟复习 sheet。
- 每天一行闭环：Focus -> 练习/反馈信号 -> 迭代动作。

模式：

- Pass-only：优先标准题、定义/公式、常见模板和保底分。
- High-score：加入难变式、证明、综合题和完整限时模考。
- Cram：砍掉低收益阅读，用考前一页纸、标准方法和短循环刷题抢分。
- Multi-course：按考试日期、难度、学分/重要性和当前薄弱程度排序。

## Exam Ecology Templates (考试生态模板)

不同考试形式决定不同的复习策略。根据考试生态类型自动适配：

| 生态类型 | 资料优先级 | 练习形式 | 最后 48 小时策略 | 是否需要一页纸 |
|---|---|---|---|---|
| `闭卷-背诵型` (政治/法学/管理) | 老师PPT > 往年题 > 教材 | 名词解释+简答+论述模板+关键词默写 | 高频关键词速记+模板背诵 | 不适用（闭卷） |
| `闭卷-计算型` (高数/物理/电路) | 公式表 > 往年题 > PPT例题 | 限时计算+条件回忆+方法识别 | 公式条件速记+3套限时小题 | 不适用 |
| `闭卷-证明型` (数学分析/抽象代数) | 定理条件 > 证明模板 > 往年题 | 证明骨架补全+条件回忆+反例 | 核心定理条件速记+证明框架 | 不适用 |
| `开卷-检索型` (部分工程/法学) | 教材目录 > 法条索引 > 笔记 | 快速检索定位+应用分析 | 标签/索引系统整理+练定位速度 | ✅ 索引页 |
| `一页纸` (半开卷) | 公式+条件+模板+易错点 | 一页纸制作+限时练习+检索练习 | 一页纸定稿+用一页纸限时做题 | ✅ 核心 |
| `OJ/机考` (编程/算法) | 题型模板 > OJ真题 > 算法笔记 | 真实输入输出+边界+TLE/WA诊断 | 模板复习+2套限时OJ | 不适用 |
| `实验考/操作考` | 实验指导书 > 操作视频 > 往年viva | 操作步骤排序+异常诊断+口试问答 | 步骤默写+仪器checklist+viva模拟 | ✅ 步骤卡 |
| `口试/答辩` | 核心概念 > 追问链 > 往年题 | 口试阶梯+追问训练+限时表达 | 高频问题过一遍+30秒模板 | 不适用 |
| `PPT驱动型` (老师PPT=考试范围) | PPT星标页 > 课堂笔记 > 教材 | PPT关键词+星标页专练 | 星标页速记+PPT关键词默写 | 不适用 |
| `往年题驱动型` (题型固定换数字) | 3-5年往年题 > PPT > 教材 | 题型识别+往年题变式 | 往年题限时重做+易错点速记 | 不适用 |

在 `/profile` 和 `/plan` 阶段根据考试形式自动选择生态模板。用户不需要记模板名——从"闭卷""开卷""机考""实验考"等关键词自动匹配。

默认每日块结构：

1. 阅读前先做预检或主动回忆热身。
2. 修复最弱点或讲解最关键概念。
3. 做练习；基础稳定后改成交错练习。
4. 错题修复并要求自我解释。
5. 更新 SRS 和下一次到期复习。

中文 `/plan` 默认模板：

```markdown
## 目标与约束
- 距离考试:
- 每天可用时间:
- 目标:
- 资料置信度:

## 复习优先级
| 优先级 | 章节/主题 | 为什么先学 | 今日动作 |
|---|---|---|---|

## 每日计划
| 天 | 底线任务 | 可选加分 | 练习/反馈 | 本轮闭环 |
|---|---|---|---|---|

## 不要花太多时间
[低收益内容或暂时放弃项]

## 下一步
[一个马上开始的任务]
```

## Cram Mode

Use when time remaining is short or the user explicitly requests `/cram`.

- 从得分收益出发，不从章节顺序出发。
- 聚焦标准方法、公式条件、常见坑和高频题型。
- 用短练习闭环替代长摘要。
- 产出考前一页纸和简短“不要浪费时间”列表。

### Managing Exam Anxiety

Late-stage cramming is as much an emotional state as a knowledge gap; a panicking student retains little. Without being saccharine:

- **先给 quick win。** 先安排一个现在就能拿下的高收益点，打断慌乱，再进入难点。
- **范围有限且具体。** “3 个主题，90 分钟”比“全都复习”更可执行。
- **允许取舍。** 明确告诉学生跳过低收益内容是策略，不是失败。
- **保住基础分。** 定义、公式条件和标准模板通常比押最难题更稳。
- 语气冷静、直接，给下一个动作，不讲学习方法大道理。

## Last Page

考前最后复习，生成紧凑 sheet：

- 必背定义/公式。
- 标准题模板。
- 常见坑。
- 时间分配。
- 交卷前检查项。
- 实验课：步骤、数据表、误差分析、viva Q&A。

中文 `/last-page` 模板：

```markdown
# 考前一页纸

## 必背
## 标准模板
## 易错点
## 时间分配
## 交卷前检查
## 最后 30 分钟
```

In ima-native environments, build `/last-page` from `/source-map`, `/teacher-emphasis`, the Weak Point Board, SRS due items, and high-yield formulas/templates. Prefer writing it to ima-note; use it as the default input for `/ppt`.

## Dashboard

For `/dashboard`, generate a Markdown dashboard instead of relying on the local terminal dashboard:

```markdown
# 复习仪表盘

## 今日状态
- 距离考试:
- 当前目标:
- 今日必须完成:

## 考试就绪度（Exam Readiness）
- P0 考点覆盖率: [exam-ready / total P0]%
- 限时正确率: [%]
- 高信心错题: [N] 个 ⚠
- 提示依赖考点: [N] 个 ⚠
- 最大风险: [top 2 risks]
- 最高收益动作: [one action]

## 掌握度热力图
[topic progress bars]

## 错误类型分布
[error-category table from wrong notes; see `references/wrong-note.md` → Error-Type Analytics. Omit if no wrong notes yet.]

## 高信心错题预警
[列出 confidence_gap >= 2 的主题，这些是考试最危险的"以为会了但会丢分"的点]

## 今日待复习
| Topic | 原因 | 建议动作 |
|---|---|---|

## 级联风险
[列出 mastery_band == weak 且有 prerequisites gap 的主题，标注需先修的前置概念]

## 最大风险
1.
2.
3.

## 下一步
```

考试就绪度数据来自 `references/adaptive-state.md` 的 Exam Readiness Assessment。没有足够数据时，标注"数据不足，需要更多练习才能评估就绪度"，不要编造百分比。

In ima-native environments, gather data from `memory_recall`, `search source=note`, the course homepage, SRS table, weak-point board, and recent wrong notes. Update the dashboard through `ima-note` when available.

仪表盘必须包含 `references/adaptive-state.md` 定义的”下一步推荐”表，并只把排名第一的动作设为”今日必须完成”。其余动作进入候选队列，避免同时开启过多任务。

## Multi-Course Exam Week Scheduling (多课程期末周调度)

很多中国大学生一周 3-5 门考试。当用户有多门课程时，`/plan` 必须做跨课程优先级排序，不能只按课程顺序排：

### 排序维度

| 维度 | 权重 | 说明 |
|---|---|---|
| 考试日期 | 最高 | 最近的考试优先 |
| 学分/挂科风险 | 高 | 高学分、挂科边缘的课优先 |
| 当前掌握度 | 高 | 掌握度越低越需要时间 |
| 提分弹性 | 中 | 从 50→60 比从 85→90 更容易 |
| 每天可用时间 | 中 | 现实约束 |
| 认知切换成本 | 低 | 背诵课与计算课交替安排，减少同类疲劳 |

### 调度原则

1. **按考试日期倒排**：最近的考试分配最多时间。
2. **保底优先**：挂科边缘的课先确保及格线，再冲高分课。
3. **背诵/计算交替**：同一天不要连续安排 4 小时背诵或 4 小时计算，交替安排减少认知疲劳。
4. **考前一天只复习该门**：考试前一天只安排该门课的最后复习（考前一页纸 + 速记 + 易错点），不安排新内容。
5. **考后释放时间**：某门考完后，把释放的时间块分配给下一门。

### 多课程计划模板

```markdown
## 期末周多课程调度
| 日期 | 上午 | 下午 | 晚上 | 备注 |
|---|---|---|---|---|
| 周一 | 高数(计算) | 马原(背诵) | 高数(模考) | 周三考高数 |
| 周二 | 高数(冲刺) | 高数(一页纸) | 数据结构(基础) | 高数考前最后复习 |
| 周三 | ★高数考试★ | 数据结构(刷题) | 马原(背诵) | 考后释放给后面 |
| 周四 | 数据结构(模考) | 马原(论述模板) | 数据结构(错题) | 周五考数据结构 |
| 周五 | ★数据结构考试★ | 马原(冲刺) | 马原(模考) | |
| 周六 | ★马原考试★ | 休息 | | |

## 风险评估
- 高数：掌握度 60%，挂科风险中，需重点突破积分换元
- 数据结构：掌握度 45%，挂科风险高，需先修树和图
- 马原：掌握度 70%，挂科风险低，背诵抓手足够
```
