class LLMClient:
    def __init__(self):
        pass

    def ask(self, prompt: str) -> str:
        # Minimal rule-based stub: replace with real model calls later.
        if "步骤" in prompt or "当前步骤" in prompt:
            return "执行整理桌面，并准备完成任务。"
        return "继续检查状态。"
class LLMClient:
    def __init__(self):
        pass

    def ask(self, prompt: str) -> str:
        if "步骤" in prompt:
            return "执行整理桌面，并准备完成任务。"
        return "继续检查状态。"
