# my-agent

一个最小可运行的 Python agent 项目示例，演示 agent 结构、环境、prompt 管理和模型交互的基本设计。

## 目录结构

- [pyproject.toml](pyproject.toml) - 项目配置和依赖
- [src/my_agent/](src/my_agent/) - 源码包
  - [src/my_agent/agent.py](src/my_agent/agent.py#L1) - `Agent` 主逻辑
  - [src/my_agent/env.py](src/my_agent/env.py#L1) - `Environment` / 任务模拟
  - [src/my_agent/prompt_manager.py](src/my_agent/prompt_manager.py#L1) - prompt 生成
  - [src/my_agent/llm_client.py](src/my_agent/llm_client.py#L1) - 模型接口抽象
- [src/my_agent/examples/run_agent.py](src/my_agent/examples/run_agent.py#L1) - 运行示例
- [tests/test_agent.py](tests/test_agent.py#L1) - 简单单元测试

## 快速启动

1. 进入项目目录

```bash
cd /Users/emilycui/git/my-agent
```

2. 创建并激活虚拟环境

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. 安装项目和开发依赖

```bash
pip install -e .\[dev\]
```

> 注意：在 `zsh` 下需要用反斜线或引号避免方括号被 shell 扩展，例如 `pip install -e .\[dev\]` 或 `pip install -e " .[dev]"`。

4. 运行示例

```bash
python src/my_agent/examples/run_agent.py
```

5. 运行测试

```bash
pytest tests
```

## 设计思路

- `Agent` 负责决策循环：获取观察、生成 prompt、调用模型、执行动作
- `Environment` 负责任务状态和动作反馈
- `PromptManager` 将观察转成 prompt，方便后续改模板
- `LLMClient` 抽象模型接口，后续可切换为真实 API / 本地模型

## 为什么这样设计

- 独立模块让项目更易扩展
- 先用“模拟环境 + 规则模型”跑通基本流程
- 后续可以单独替换 `llm_client.py` 为真实 LLM
- 这个结构适合作为小 agent 的入门参考

## 示例输出

运行 `python src/my_agent/examples/run_agent.py` 将打印类似：

```
Step 1:
  Observation: {'step': 0, 'goal': '整理桌面'}
  Action: 执行整理桌面，并准备完成任务。
  Result: {'done': False, 'reward': 1, 'info': {'action': '执行整理桌面，并准备完成任务。'}}

...
```

## 如何替换为真实 LLM

`src/my_agent/llm_client.py` 是一个最小的 stub，方便后续替换。

- 如果要调用 OpenAI API：在 `LLMClient.ask()` 中集成 `openai` 客户端，或使用 `langchain` 的包装器。
- 如果要使用本地模型（如 `transformers` 或 `llama-cpp-python`）：在 `LLMClient` 内加载模型并返回生成结果。

示例（伪代码）：

```py
from openai import OpenAI

class LLMClient:
    def __init__(self, api_key: str):
        self.client = OpenAI(api_key=api_key)

    def ask(self, prompt: str) -> str:
        resp = self.client.chat.completions.create(model="gpt-4o", messages=[{"role":"user","content":prompt}])
        return resp.choices[0].message.content
```

记得把密钥等敏感信息放到 `.env` 或系统环境变量，并把 `.env` 列入 `.gitignore`（已包含）。

## 贡献

欢迎改进：

- 修复 bug 或添加测试 → 提交 PR
- 扩展 `LLMClient` 以支持更多后端
- 提供更多示例场景和 benchmark

请遵循简短的贡献流程：fork → 新分支 → commit → PR。
