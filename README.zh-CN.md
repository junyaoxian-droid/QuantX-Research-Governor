# QuantX Research Governor 中文说明

QuantX Research Governor 是一套面向 AI 辅助量化研究的协议和模板库。

它不是策略仓库，不包含真实信号、真实持仓、私有数据或收益承诺。  
它关注的是量化研究本身如何更规范：

- 先提出市场假设；
- 再做因子/标签验证；
- Train / Validation / Test 分离；
- Validation 选参，Test 只评估；
- 加入成本压力和 cadence 压力；
- 记录失败候选；
- 重要结果交给另一个环境 source replay；
- 把人工判断与模型证据分开。

如果 `QuantX-GoalForge` 是通用的 Codex Goal 治理框架，那么本仓库就是量化研究专用协议层。

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
