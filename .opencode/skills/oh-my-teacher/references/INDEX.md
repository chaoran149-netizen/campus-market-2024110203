# References Index

执行任何命令前，先加载对应 reference。本文件是命令路由、命令说明和环境降级策略的唯一事实来源。

## 加载顺序（Load Order）

| 优先级 | 文件 | 用途 | 何时加载 |
|----------|------|---------|-----------|
| 1 | `course-profiles.md` | 课程画像、Current Course Snapshot、多课程切换和持久化格式 | `/profile`, `/materials`, `/diagnose`, `/plan`, `/map`, `/mock`, `/grade`, `/fix`, `/quiz`, `/oral`, `/group-quiz`, `/summary`, `/resume`, course switch |
| 2 | `environment-adaptation.md` | 判断宿主能力并选择降级方案 | 涉及文件、检索、shell/scripts、持久化、引用、图示、代码演示、导出或未知环境 |
| 3 | `materials-ingestion.md` | 摄取 PDF/PPT/笔记/往年题，提取知识清单、重点和缺口 | `/materials` 或用户上传课程资料 |
| 4 | `material-retrieval.md` | 无外部资料或信息很少时的资料检索、查询词和来源等级 | 用户只给课程名、资料缺失、检索课程资料或 `/materials` 资料很薄 |
| 5 | `subject-adaptation.md` | 按学科调整严谨度、符号、例子、题型和图示 | 已建立课程画像后的任何复习任务 |
| 6 | `interaction-modes.md` | 选择苏格拉底、费曼、阅卷人、冲刺等教学模式 | 生成题目、讲解、反馈或切换模式前 |
| 7 | `learning-strategies.md` | 主动回忆、间隔复习、交错练习等学习策略 | `/plan`, `/quiz`, `/fix`, `/socratic`, `/feynman`, `/flashcards` 或选择学习方法时 |
| 8 | `ima-adaptation.md` | ima-native 工具、记忆、笔记、知识库、报告和 PPT 路由 | 环境是 ima，用户提到 ima/知识库/笔记，或工具含 ask_user/fetch/search/memory/use_skill |
| 9 | `chinese-routing.md` | 中文自然语言触发词到命令/工作流的映射 | 中文请求没有斜杠命令，或暗示中文知识库/笔记学习流 |
| 10 | `agent-adapter-contract.md` | 多 Agent 适配契约和能力标签 | 打包或在命名 Agent 运行 skill |
| 11 | `agent-optimization.md` | 按 Agent 能力选择最佳执行路径 | 运行、打包、验证或调试 Agent 适配 |
| 12 | `agent-inventory.md` | 各 Agent 能力清单和不确定项 | 添加、验证或调试 Agent 适配 |
| 13 | `staged-review-workflow.md` | 两阶段“资料到练习”流程和 Stage 1 核心复习包 | 用户要阶段式复习、核心材料或最值得学的章节 |
| 14 | `focus-feedback-iteration.md` | 聚焦 - 反馈 - 迭代闭环 | 多步骤复习、计划、练习、批改、修复、总结或阶段工作流 |
| 15 | `opt-in-reminders.md` | 明确 opt-in 的提醒和每日/每周知识归纳契约 | 用户明确要求启用、修改、停止或生成提醒/归纳卷 |
| 16 | `adaptive-state.md` | 轻量掌握度、支架消退、前置阻塞、级联失效追溯、考试就绪度和下一步推荐规则 | `/plan`, `/dashboard`, `/summary`, `/quiz`, `/fix`, `/readiness`, reminders 或需要排序下一步时 |
| 17 | `course-wiki.md` | 课程知识库（LLM Wiki）：不可变原始源 + 互联页面 + Ingest/Query/Lint | `/wiki`, `/wiki-ask`, `/wiki-lint`，或用户要把资料沉淀成可累积、可互链的课程知识库 |
| 18 | `exam-psychology.md` | 考试心理与临场策略：审题分流、卡题恢复、焦虑重评、考前流程、交卷检查 | `/exam-routine`, `/mock` 考前训练, `/cram` 焦虑管理, 考试临场策略 |

只有用户要求示例会话、输出样例、行为对比或回归参考时，才加载 `examples/`。

## 命令目录与参考映射（Command Catalog）

| 命令 | 中文别名 | 说明 | 主参考 | 辅助参考 |
|---------|----------|-------------|-------------------|---------------------|
| `/help` | `/帮助` | 按阶段列出命令、用途和中文例句 | This index | - |
| `/profile` | `/建档` | 建立课程画像，只问真正缺失的关键信息 | `course-profiles.md` | `course-templates.md`, `scripts/course_templates.py` |
| `/materials` | `/资料` | 摄取上传/粘贴的课件、笔记、题库、往年题；资料不足时先检索并标注来源等级 | `materials-ingestion.md` | `course-profiles.md`, `environment-adaptation.md`, `material-retrieval.md` |
| `/source-map` | `/来源图` | 基于来源建立资料覆盖图、重点来源、缺口和引用锚点 | `ima-adaptation.md` | `materials-ingestion.md`, `review-plans.md` |
| `/paper` | `/考卷` | 针对闭卷、开卷、半开卷等笔试优化复习 | `course-profiles.md` | `subject-adaptation.md` |
| `/paper-analyze` | `/分析真题` | 分析往年题、样卷、作业题和题库，反推高频考点 | `exam-paper-analysis.md` | `ima-adaptation.md`, `course-profiles.md` |
| `/teacher-emphasis` | `/划重点` | 提取老师划重点、课堂强调、星标页、复习提纲和答疑信号 | `ima-adaptation.md` | `materials-ingestion.md`, `review-plans.md` |
| `/lab` | `/实验` | 针对实验考、实验报告、操作考和 viva/口试优化复习 | `course-profiles.md` | `subject-adaptation.md` |
| `/diagnose` | `/诊断` | 用约 5 题快速定位跨章节薄弱点 | `question-types.md` | `course-profiles.md`, `practice-workflows.md` |
| `/plan` | `/计划` | 生成可执行的 1/3/7/14/30 天复习计划 | `review-plans.md` | `course-profiles.md`, `subject-adaptation.md`, `material-retrieval.md` |
| `/map` | `/图谱` | 输出知识图谱、考试地图、公式/定义和优先级 | `review-plans.md` | `course-profiles.md` |
| `/explain [topic]` | `/讲解` | 讲清一个概念：定义、直觉、例题、陷阱、回忆题 | `subject-adaptation.md` | `interaction-modes.md` |
| `/socratic [topic]` | `/追问` | 苏格拉底式引导：一次一个问题，先提示再给答案 | `socratic-mode.md` | `interaction-modes.md`, `learning-strategies.md`, `subject-adaptation.md` |
| `/feynman [topic]` | `/费曼` | 费曼复述检查：学生讲，AI 挑漏项、追问并批改 | `feynman-mode.md` | `interaction-modes.md`, `subject-adaptation.md` |
| `/quiz` | `/刷题` | 自适应刷题，按表现升降难度 | `question-types.md` | `interaction-modes.md`, `subject-adaptation.md`, `course-profiles.md`, `adaptive-state.md` |
| `/mock` | `/模考` | 生成限时模拟卷、答案和评分 rubric | `practice-workflows.md` | `question-types.md`, `course-profiles.md` |
| `/oral` | `/口试` | 模拟口试/答辩，逐问追问并给反馈 | `practice-workflows.md` | `interaction-modes.md`, `subject-adaptation.md` |
| `/grade` | `/批改` | 严格批改用户答案，定位扣分点和错因 | `question-types.md` | `course-profiles.md`, `practice-workflows.md`, `spaced-repetition.md`, `adaptive-state.md` |
| `/fix` | `/修复` | 针对薄弱点给微课、变式题和修复练习 | `practice-workflows.md` | `question-types.md`, `subject-adaptation.md`, `adaptive-state.md` |
| `/flashcards` | `/闪卡` | 生成主动回忆卡片；需要时用 `scripts/export_flashcards.py` 导出 CSV/TSV | `SKILL.md` | `practice-workflows.md`, `learning-strategies.md`, `environment-adaptation.md` |
| `/review-due` | `/到期复习` | 查看今天到期的间隔复习主题 | `spaced-repetition.md` | `course-profiles.md` |
| `/group-quiz` | `/抢答` | 组织多人小组问答、抢答或轮流讲解 | `group-study.md` | `question-types.md`, `subject-adaptation.md` |
| `/visual` | `/图示` | 生成图示、流程图、概念图或图像 prompt | `visual-generation.md` | `subject-adaptation.md`, `environment-adaptation.md` |
| `/video` | `/视频` | 生成分镜、动画方案或视频 API 工作流 | `visual-generation.md` | `environment-adaptation.md` |
| `/code-demo` | `/演示` | 生成可运行代码演示、算法追踪或仿真 | `coding-demos.md` | `subject-adaptation.md`, `environment-adaptation.md` |
| `/cram` | `/冲刺` | 进入考前冲刺/抢分模式，优先高收益内容 | `review-plans.md` | `interaction-modes.md` |
| `/last-page` | `/一页纸` | 生成考前一页纸：公式、模板、陷阱、时间分配、交卷检查 | `review-plans.md` | `ima-adaptation.md`, `materials-ingestion.md` |
| `/dashboard` | `/仪表盘` | 生成复习仪表盘：状态、热力图、到期主题、风险和下一步 | `review-plans.md` | `ima-adaptation.md`, `spaced-repetition.md`, `course-profiles.md`, `material-retrieval.md` |
| `/resume` | `/恢复` | 从粘贴的 Course Snapshot 恢复上下文 | `course-profiles.md` | - |
| `/summary` | `/总结` | 输出本轮复盘：练了什么、正确率变化、弱点、SRS 和下一步 | `practice-workflows.md` | `course-profiles.md`, `spaced-repetition.md` |
| `/wrong-note` | `/错题本` | 从批改/刷题/模考反馈生成错题本并同步 SRS 摘要 | `wrong-note.md` | `question-types.md`, `spaced-repetition.md`, `ima-adaptation.md` |
| `/report` | `/报告` | 在可用时通过 ima-report 生成阶段复盘或覆盖率报告 | `ima-adaptation.md` | `exam-paper-analysis.md`, `review-plans.md` |
| `/ppt` | `/幻灯片` | 在可用时通过 ima-ppt 生成考前冲刺或错题复盘 PPT | `ima-adaptation.md` | `review-plans.md`, `wrong-note.md` |
| `/peer-quiz` | `/互教` | 角色逆转互教：AI 扮演糊涂同桌交错误答卷，学生批改纠错 | `interaction-modes.md` | `question-types.md`, `spaced-repetition.md` |
| `/transfer` | `/迁移` | 迁移专练：只练变式、混合题和迁移题，不练基础 | `practice-workflows.md` | `question-types.md`, `adaptive-state.md` |
| `/readiness` | `/就绪度` | 输出考试就绪度：多维度评估而非简单进度百分比 | `adaptive-state.md` | `review-plans.md`, `spaced-repetition.md` |
| `/exam-routine` | `/临场` | 考试临场策略：考前流程、卡题恢复、交卷检查 | `exam-psychology.md` | `practice-workflows.md` |
| `/calibrate` | `/校准` | 信心-表现校准专练：找出高信心错题 | `learning-strategies.md` | `question-types.md`, `adaptive-state.md` |
| `/reflect` | `/反思` | 齐默曼式复盘反思：目标-完成-校准-下一步 | `practice-workflows.md` | `adaptive-state.md`, `focus-feedback-iteration.md` |
| `/mode [mode-name]` | `/模式` | 显式切换当前任务的互动模式 | `interaction-modes.md` | - |
| `/wiki` | `/百科` | 把资料摄取进课程知识库：建/改互联页面、更新 MOC（Ingest） | `course-wiki.md` | `materials-ingestion.md`, `staged-review-workflow.md`, `environment-adaptation.md` |
| `/wiki-ask [question]` | `/百科问` | 先查 wiki 页面再合成带引用答案，并把新发现回填成页面（Query） | `course-wiki.md` | `material-retrieval.md`, `ima-adaptation.md` |
| `/wiki-lint` | `/百科检查` | 知识库体检：孤页、断链、缺来源、矛盾、考点覆盖缺口（Lint） | `course-wiki.md` | `exam-paper-analysis.md`, `spaced-repetition.md` |

英文命令和中文别名完全等效，用户输入任意一种均按相同流程执行。中文别名的完整映射表见 `chinese-routing.md` → 中文命令别名。

用户显式命令只覆盖当前任务的自动模式选择。除非用户要求保持某个模式，完成当前任务后回到自动选择。

### `/help` Output Template

When the user runs `/help`, use this exact structure:

```markdown
# Oh My Teacher — 命令

英文命令和中文别名都能用，效果完全一样。也可以直接说中文需求，不必记命令。
例如：”还有三天考试救一下””帮我分析这套往年题””按考试标准批改我的答案”。

## 建档与资料
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /profile | /建档 | 建立课程画像 |
| /materials | /资料 | 整理课程文件、笔记和题库 |
| /source-map | /来源图 | 基于来源生成资料覆盖图 |
| /diagnose | /诊断 | 5 题快速诊断水平 |
| /paper | /考卷 | 针对闭卷/开卷笔试优化 |
| /paper-analyze | /分析真题 | 分析往年题和出题规律 |
| /teacher-emphasis | /划重点 | 提取老师划重点 |
| /lab | /实验 | 针对实验考优化 |

## 知识库
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /wiki | /百科 | 把资料沉淀成互联课程知识库 |
| /wiki-ask | /百科问 | 基于知识库提问并带引用作答 |
| /wiki-lint | /百科检查 | 知识库体检：孤页/断链/缺口 |

## 计划
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /plan | /计划 | 按天生成复习计划 |
| /map | /图谱 | 知识图谱和考试优先级 |
| /last-page | /一页纸 | 考前一页纸 |
| /dashboard | /仪表盘 | 复习仪表盘 |

## 练习
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /quiz | /刷题 | 自适应刷题 |
| /mock | /模考 | 限时模拟卷（含审题分流训练） |
| /oral | /口试 | 口试/答辩模拟 |
| /grade | /批改 | 严格批改（含踩点分析和认知诊断） |
| /fix | /修复 | 修复薄弱点（含渐进示范消退） |
| /group-quiz | /抢答 | 多人小组问答 |
| /peer-quiz | /互教 | 角色逆转互教（AI做错题，你来批改） |
| /transfer | /迁移 | 迁移专练（变式/混合/迁移题） |
| /calibrate | /校准 | 信心-表现校准专练 |

## 讲解
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /explain | /讲解 | 讲解一个概念 |
| /socratic | /追问 | 苏格拉底式追问 |
| /feynman | /费曼 | 费曼复述检查 |
| /visual | /图示 | 图示和可视化讲解 |
| /video | /视频 | 分镜或动画方案 |
| /code-demo | /演示 | 可运行代码演示 |

## 追踪与导出
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /review-due | /到期复习 | 今日到期间隔复习 |
| /wrong-note | /错题本 | 生成错题本（含误区诊断） |
| /flashcards | /闪卡 | 生成/导出闪卡 |
| /summary | /总结 | 本轮学习复盘 |
| /reflect | /反思 | 齐默曼式复盘反思 |
| /resume | /恢复 | 从快照恢复上下文 |
| /report | /报告 | 阶段复盘报告 |
| /ppt | /幻灯片 | 考前冲刺 PPT |

## 考试策略
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /readiness | /就绪度 | 考试就绪度评估 |
| /exam-routine | /临场 | 考前/考中/交卷流程 |

## 模式
| 命令 | 中文别名 | 说明 |
|------|----------|------|
| /mode | /模式 | 切换互动模式 |
| /cram | /冲刺 | 考前抢分模式 |
| /help | /帮助 | 查看所有命令 |

直接用中文说你现在需要什么，我会自动识别并执行对应命令。英文和中文命令效果一样。

💡 每轮任务完成后，我会根据你的复习进度和状态推荐 2-3 个下一步供你选择。
```

## 环境降级一览（Environment Fallbacks）

详细降级方案见 `environment-adaptation.md`。下表是路由概览：

| Command | Agent shell | RAG notebook | Notes app | Plain chat |
|---------|-------------|--------------|-----------|------------|
| `/materials` | Read files; use PDF/PPT/text tooling; search local workspace when material is missing | Cite from document context; search RAG corpus when thin | Ingest Markdown notes, backlinks, tags, pasted excerpts | Ask student to paste chapter text or output copyable search queries |
| `/flashcards` | Write Markdown, then run `scripts/export_flashcards.py` | Emit Markdown cards inline | Emit Markdown cards with tags/backlinks | Emit Markdown cards inline |
| `/visual` | Mermaid, HTML, Manim, Python plot, or image prompt as appropriate | Mermaid or ASCII inline | Mermaid/Markdown tables if supported; otherwise ASCII | ASCII diagrams or numbered step lists |
| `/video` | Storyboard plus Manim/HTML Canvas plan or file when tools exist | Storyboard inline | Storyboard Markdown | Storyboard inline only; never call video API |
| `/code-demo` | Write and run a file; show output | Code block plus expected output | Code block plus trace note | Code block plus expected output and walkthrough |
| `/plan` | Write `plan.md` when useful | Plan inline | Markdown plan with tags/backlinks | Plan inline plus copy/pin reminder |
| `/map` | Mermaid or Markdown file when useful | Mermaid or ASCII inline | Mermaid/Markdown concept map | ASCII concept map |
| `/mock` | Write `mock.md` and `answer.md` when useful | Mock inline | Mock as Markdown note | Mock inline with rubric |
| `/grade` | Read answer file and write graded artifact when useful | Grade inline with quotes/citations | Grade inline with `#错题` tags | Grade inline with quotes |
| `/explain`, `/socratic`, `/feynman`, `/quiz`, `/oral`, `/fix`, `/group-quiz` | Conversational by default | Conversational by default | Markdown-native conversational output | Conversational by default |
| `/wiki` | Build files under `.oh-my-teacher/wiki/`; run `scripts/wiki.py init/lint` | Synthesize wiki pages inline; cite document context | Native `[[links]]`, `#tags`, folders for sources/pages | Emit copyable single-page summary; accumulate per topic |
| `/wiki-ask` | grep pages then answer with `[[page]]` + source citations | Search RAG corpus; cite pages and sources | Search backlinks/tags; answer with `[[page]]` | Answer from prior pasted pages; ask to paste more |
| `/wiki-lint` | `scripts/wiki.py lint` then semantic check | Inline gap/contradiction check | Inline lint over vault pages | List likely orphans/gaps from the running summary |

## 文件概览（File Overview）

每个 reference 一行说明；按需加载，加载顺序见上方 Load Order 和 Command Catalog。

| 文件 | 内容 |
|------|------|
| `course-profiles.md` | 课程快照模板、字段规则、笔试/实验/机考/口试优化、多课程快照、磁盘格式 |
| `environment-adaptation.md` | 宿主能力检测、探测顺序、降级矩阵、各环境输出规则 |
| `agent-adapter-contract.md` | 多 Agent 适配契约、能力标签、状态/脚本策略、运行时 prompt 策略 |
| `agent-optimization.md` | Agent 启动协议、优化 profile、能力→行为映射、质量门 |
| `agent-inventory.md` | 各 Agent 能力清单、来源状态、未确认项、平台特定说明 |
| `staged-review-workflow.md` | 两阶段复习流程、最值得学的章节排序、Stage 2 模考/弱点修复 |
| `focus-feedback-iteration.md` | 聚焦-反馈-迭代闭环契约 |
| `opt-in-reminders.md` | 显式 opt-in 提醒、主动消息能力规则、每日/每周知识归纳、弱点和记忆目标推送 |
| `adaptive-state.md` | 掌握度分层、支架消退、前置阻塞、级联失效追溯、考试就绪度、信心差距、提示依赖、迁移水平、确定性下一步排序 |
| `course-wiki.md` | 课程知识库（LLM Wiki）：不可变原始源、互联页面、页面分类/模板、Ingest/Query/Lint、集成钩子、降级 |
| `ima-adaptation.md` | ima-native 协议：14 个工具、5 个技能、来源等级、笔记优先持久化、知识库检索、报告、PPT、命令覆盖 |
| `chinese-routing.md` | 中文自然语言→命令/工作流路由映射 |
| `materials-ingestion.md` | PDF/PPT/笔记/往年题摄取、提取目标、输出契约、增量+多文件合并、各环境摄取 |
| `material-retrieval.md` | 缺失资料检索协议、来源等级、查询词组、证据表、无来源降级 |
| `subject-adaptation.md` | 按学科调整严谨度、符号、例子、图示（数学/物理/CS/化生医/文社科/语言/设计/工程/临床） |
| `interaction-modes.md` | 教学模式选择、角色逆转互教、渐进示范消退、防依赖规则、混合模式、回答契约、模式切换 |
| `socratic-mode.md` | `/socratic` 协议：一次一问、提示阶梯、假设追问、反例、学生总结、收束 |
| `feynman-mode.md` | `/feynman` 协议：学生讲解、追问挑错、评分、重讲、修复卡、SRS 更新 |
| `learning-strategies.md` | 循证学习策略：检索练习、间隔、交错、精细加工、自我解释、具体例子、双编码、预测试、类比、信心校准 |
| `review-plans.md` | 知识图谱、复习计划、冲刺模式（含焦虑管理）、热力图、考前一页纸、仪表盘 |
| `exam-paper-analysis.md` | 往年题分析：分布、高频考点、得分模式、证据范围、ima 笔记更新 |
| `practice-workflows.md` | 主动回忆、模考（含审题分流和时间管理）、错题修复（含渐进示范消退）、口试、复盘反思、复盘总结 |
| `spaced-repetition.md` | SRS 文件、主题命名/去重、间隔+ease 算法、连续重学、知识类型差异化间隔、leech 检测与级联追溯、难度所有权、`/review-due`、自动更新 |
| `wrong-note.md` | 错题本模板、误区修复字段、错因分类、ima 工作流、SRS 同步 |
| `group-study.md` | 小组问答、轮流/抢答、计分板、同伴讲解 |
| `question-types.md` | 自适应难度、出题默认、信心校准、笔试/编程/实验题型、评分 rubric、多维认知诊断、踩点给分、预测误差反思、归因训练 |
| `exam-psychology.md` | 考试流程、审题分流、卡题恢复、焦虑重评、考前检查、睡眠与精力 |
| `visual-generation.md` | 可视化选择指南、环境适配矩阵、ASCII 约定、图像 prompt + 视频分镜工作流 |
| `coding-demos.md` | 可运行演示：语言推断、状态追踪、数据结构、仿真、调试、入门约束、各环境形式 |
| `course-templates.md` | 预置课程 profile，通过 `scripts/course_templates.py` 快速建档 |
| `review-workflows.md` | 兼容重定向 → review-plans / practice-workflows / spaced-repetition / group-study |
