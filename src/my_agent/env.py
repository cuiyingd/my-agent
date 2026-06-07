class Environment:
    def __init__(self):
        self.state = {"step": 0, "goal": "整理桌面"}

    def get_observation(self):
        return {"step": self.state["step"], "goal": self.state["goal"]}

    def execute_action(self, action: str):
        self.state["step"] += 1
        done = self.state["step"] >= 3
        reward = 1 if "完成" in action else 0
        return {"done": done, "reward": reward, "info": {"action": action}}
class Environment:
    def __init__(self):
        self.state = {"step": 0, "goal": "整理桌面"}

    def get_observation(self):
        return {"step": self.state["step"], "goal": self.state["goal"]}

    def execute_action(self, action: str):
        self.state["step"] += 1
        done = self.state["step"] >= 3
        reward = 1 if "完成" in action else 0
        return {"done": done, "reward": reward, "info": {"action": action}}
