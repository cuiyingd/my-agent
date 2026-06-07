# Contributing

感谢你对 `my-agent` 的兴趣！下面是快速贡献指南，帮助你顺利提交 issue 或 PR。

1. 报告问题（Issue）
   - 使用清晰的标题描述问题或建议的功能。
   - 提供复现步骤、期望行为和实际行为，附上最小可复现示例（如果适用）。

2. 提交补丁（Pull Request）
   - Fork 仓库并在新分支上实现改动，分支名使用 `fix/xxx` 或 `feat/xxx` 风格。
   - 保持每次 PR 的改动聚焦一个主题并附上说明。
   - 在 PR 描述中列出变更点、测试步骤和相关 issue（若有）。

3. 代码风格与质量
   - 使用 `black` 格式化代码。
   - 编写或更新相应的单元测试（`pytest`）。
   - 在本地运行 `pytest tests` 确保测试通过后再提交 PR。

4. 本地开发工作流
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -e .[dev]
   pytest tests
   ```

5. 许可和行为准则
   - 本项目遵循仓库根目录的许可证（参见 `LICENSE`）。
   - 请保持 respectful 和建设性交流。

感谢你的贡献！
