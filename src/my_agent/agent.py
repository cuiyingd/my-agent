from .env import Environment
from .prompt_manager import PromptManager
from .llm_client import LLMClient


class Agent:
    def __init__(self):
        self.env = Environment()
        self.prompt_manager = PromptManager()
        self.llm = LLMClient()

    def step(self):
        obs = self.env.get_observation()
        prompt = self.prompt_manager.build_prompt(obs)
        action = self.llm.ask(prompt)
        result = self.env.execute_action(action)
        return obs, action, result

    def run(self, max_steps: int = 10):
        history = []
        for _ in range(max_steps):
            obs, action, result = self.step()
            history.append({"obs": obs, "action": action, "result": result})
            if result["done"]:
                break
        return history
from .env import Environment
from .prompt_manager import PromptManager
from .llm_client import LLMClient

class Agent:
    def __init__(self):
        self.env = Environment()
        self.prompt_manager = PromptManager()
        self.llm = LLMClient()

    def step(self):
        obs = self.env.get_observation()
        prompt = self.prompt_manager.build_prompt(obs)
        action = self.llm.ask(prompt)
        result = self.env.execute_action(action)
        return obs, action, result

    def run(self, max_steps: int = 10):
        history = []
        for _ in range(max_steps):
            obs, action, result = self.step()
            history.append({"obs": obs, "action": action, "result": result})
            if result["done"]:
                break
        return history
