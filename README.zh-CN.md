# QuantX Research Governor 中文说明

这是私有量化研究工作区所用「研究治理 skill」的可移植副本，附带配套的可复用
协议、模板与脱敏范例。

本仓库是**下游**。`SKILL.md` 及其 references 的权威归属方是私有工作区
`QuantX-Mac-Research`；这里是可以安装到别处、或在没有工作区权限时阅读的版本。
修改先在上游做，再同步过来。

仓库不含策略逻辑、信号、持仓、数据集或收益承诺。不构成投资建议，也不是交易系统。

## 它解决什么问题

Agent 做研究会漂移：中途扩大范围、悄悄复用测试集、汇报最好的那个窗口而不是当初
选中的那个、失败记录丢失。这个 skill 就是针对这些的刹车：

```text
执行前先固定 scope、预算和停止条件
Train / Validation / Test 分离，Test 只开一次
选择顺序事后不可重排
cadence、成本、rolling 压力测试是默认项而非附加项
大网格前先过 compute-scale gate
定义 iteration strength，让「N 轮迭代」指 N 次独立研究尝试，
  而不是 N 条命令或 N 个报告小节
失败记录是一等输出
recommendation 与 adoption 严格分离
```

最后一条最关键：agent 可以建议升级，但必须由人确认后才成为当前工作主线。

## 目录结构

```text
skills/quantx-research-governor/   skill 本体
  SKILL.md                         入口：路由、生命周期、安全边界
  references/                      按需加载，不一次全读
    goal_templates.md              目标 intake、plan-to-GOAL 桥接、迭代账本
    research_protocol.md           选择顺序、test ledger、placebo、压力测试
    report_contract.md             报告结构与输出文件契约
    runtime_and_resources.md       算力闸门、重跑启动、中断恢复
    subagent_policy.md             委派边界、独立复核
    governance_and_closeout.md     git 收尾、镜像仓库治理
    golden_path_fixture.md         端到端生命周期骨架
  assets/golden_path_fixture/      完整走通的生命周期样例，数据为占位符
  scripts/validate_golden_path.py  fixture 校验脚本

protocol/data-leakage-checklist.md        信任回测前的审查清单，含 A 股特有项
templates/strategy-research-report.md     策略设计规格模板
templates/research-index.md               组合层面的研究索引模板
templates/source-replay-handoff.md        独立复算交接模板
examples/sanitized-experiment-readout.md  完整 readout 范例，数字为杜撰
docs/case-study.md                        私有工作区的经验复盘
```

## 安装

见 [INSTALL.md](INSTALL.md)。简版：把 `skills/quantx-research-governor/` 复制到
你的 agent skills 目录，然后把 `SKILL.md` 里的 canonical source 表改成指向你自己
仓库的真值文件。

## 适配注意

`SKILL.md` 是按文件名做路由的——`STATE.md`、`CURRENT_SHELL_REGISTRY.md`、
`TEST_ACCESS_LEDGER.md` 等等。这些名字属于某一个特定工作区。**可复用的是路由纪律
本身，不是这些文件名**。使用前请替换成你自己的，否则 agent 会去找根本不存在的文件。

`references/report_contract.md` 同理，它规定的输出文件包假设了特定的目录布局。

## 适用对象

独立量化研究者、AI 辅助研究流程、需要报告纪律的高频回测者，以及希望在相信一个结果
之前先做可复现 source replay 的人。

## 它不是什么

不是投资建议。不是交易策略。不是信号服务。不是回测引擎。

## 沿革

`QuantX-GoalForge` 已于 2026-08-05 归档并并入本仓库。它的 goal governance 文档、
prompt 模板和两个 `goal-governor` skill 均被 `references/goal_templates.md` 覆盖
（后者是严格超集）。唯一值得保留的案例复盘，现为 `docs/case-study.md`。
`protocol/protocol-v2.md` 同样被 `references/research_protocol.md` 取代并删除。
两个仓库的完整历史已保存为本地 git bundle。

## License

MIT，见 [LICENSE](LICENSE)。
