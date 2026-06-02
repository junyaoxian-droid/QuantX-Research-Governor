# QuantX Research Governor 中文说明

QuantX Research Governor 是一套面向 AI 辅助量化研究的协议和模板库。

它不是策略仓库，不包含真实信号、真实持仓、私有数据或收益承诺。  
它关注的是量化研究本身如何更规范：

- 先提出市场假设；
- 再做因子/标签验证；
- Train / Validation / Test 分离；
- Validation 选参，Test 只评估；
- 对时间序列策略加入 rolling walk-forward，滚动窗口验证；
- 加入成本压力和 cadence 压力；
- 在大网格前先做 compute-scale gate，估算计算规模，再选择全量、分阶段或多阶段漏斗；
- 增加 efficiency modes，让简单查询保持轻量，大型实验才完整治理；
- 重实验运行期间不空等，要提前写出预期结果、失败分支、下一轮迭代方向；
- subagent 和并行只用于独立审计、固定回放、报告 QA 或 handoff，不让它们决定最终升级；
- 输出 Sharpe、Calmar、胜率、最大回撤、换手率等标准指标；
- 记录失败候选；
- 增加 adoption gate，把 agent 建议和用户确认采用分开；
- 重要结果交给另一个环境 source replay；
- 把人工判断与模型证据分开。

如果 `QuantX-GoalForge` 是通用的 Codex Goal 治理框架，那么本仓库就是量化研究专用协议层。

## 重型 Goal 契约

对于重型、模糊、或可能影响策略治理的量化研究，不要只依赖原生 goal 的一句短摘要。执行前应先创建本地 `GOAL.md`，记录：

- 用户回答与假设；
- 明确的迭代强度或失败预算；
- Train / Validation / Test 与 rolling 要求；
- 计算漏斗和进入 full-run 的条件；
- 成功、部分成功、失败和停止规则；
- 输出路径；
- 禁止事项。

如果用户说“迭代 5 次”，应理解为 5 个独立研究假设或修复机制，而不是 5 条命令、5 张图、5 次重跑或 5 个报告小节。

## 计算规模闸门

严格研究不等于无脑全量。大型回放或压力测试开始前，应先估算：

```text
replay units = candidates * cadences * costs * overlays * rolling windows
```

如果规模过大，优先采用分阶段漏斗：先用主执行口径和基准成本筛出候选，
再对真正有价值的候选逐步增加 cadence、cost、industry、execution、rolling
等压力测试。阶段数不是固定的；小实验可以直接全量，大实验可以两阶段或多阶段。

这不是降低严谨性，而是避免把已经失败的候选送进所有昂贵压力测试。

## 效率模式

研究治理要和任务风险匹配。

| 模式 | 适用场景 | 处理方式 |
|---|---|---|
| `quick_monitor` | 最新信号、持仓复盘、一张表 | 只读当前 Hub 和相关最新报告 |
| `standard_check` | 单个假设或小回放 | 固定范围、轻量报告、最小验证 |
| `governance_patch` | 记忆、Hub、索引清理 | 只改目标治理文件 |
| `heavy_experiment` | 大搜索、滚动验证、升级证据 | 完整协议、分阶段计算漏斗、升级采用闸门 |

简单 monitor 不需要完整 TVT/rolling/cost/cadence 流程；但可能改变主线的实验不能跳过这些流程。

## 升级采用闸门

研究报告可以给出“建议升级”，但不能自动改写当前策略层级。每次重要实验后，
先输出 adoption table：

| 分类 | 含义 |
|---|---|
| `recommended_upgrade` | 证据足够强，建议升级，但等待人工确认 |
| `source_replay_candidate` | 值得在源环境复现 |
| `paper_shadow_candidate` | 值得跟踪，不作为主线 |
| `manual_review_candidate` | 只辅助人工复核 |
| `diagnostic_only` | 有解释力，不可执行 |
| `stop_as_rule` | 停止作为规则推进 |

只有研究负责人确认哪些实验线升级、保留或淘汰后，才更新研究地图、README
或其他项目 source-of-truth 文件。skill 描述的是流程行为，不保存当前策略事实；
只有用户明确要求调整研究流程时才修改 skill。这样可以避免每轮实验后出现一堆
互相竞争的“主线”。

## 不包含什么？

- 不包含投资建议；
- 不包含交易策略；
- 不包含自动交易；
- 不包含真实账户信息；
- 不包含每日信号；
- 不包含私有数据。

## 适合谁？

- 独立量化研究者；
- 用 Codex / LLM 做回测和实验的人；
- 需要管理大量实验报告的人；
- 想减少未来函数、过拟合、OOS 诱惑的人；
- 需要 Windows/Mac 或多环境复现的人。

## 社区共建

欢迎量化研究者、Codex 用户、回测工程师、数据科学实践者一起贡献想法。

有价值的贡献包括：更好的验证清单、滚动窗口模板、未来函数审计案例、source replay 流程、指标定义、脱敏失败案例等。这个仓库的目标不是追求更漂亮的回测，而是让量化研究协议更可靠、更容易复核、更方便其他人接手。
