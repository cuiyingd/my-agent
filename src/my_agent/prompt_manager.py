class PromptManager:
    def build_prompt(self, observation: dict) -> str:
        return (
            "你是一个智能 agent。\n"
            f"当前步骤: {observation['step']}\n"
            f"目标: {observation['goal']}\n"
            "请给出下一步动作。"
        )
class PromptManager:
    def build_prompt(self, observation: dict) -> str:
        return (
            "你是一个智能 agent。\n"
            f"当前步骤: {observation['step']}\n"
            f"目标: {observation['goal']}\n"
            "请给出下一步动作。"
        )
