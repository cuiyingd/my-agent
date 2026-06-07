from my_agent import Agent


def main():
    agent = Agent()
    history = agent.run(max_steps=5)
    for step, record in enumerate(history, 1):
        print(f"Step {step}:")
        print("  Observation:", record["obs"])
        print("  Action:", record["action"])
        print("  Result:", record["result"])
        print()


if __name__ == "__main__":
    main()
from my_agent import Agent

def main():
    agent = Agent()
    history = agent.run(max_steps=5)
    for step, record in enumerate(history, 1):
        print(f"Step {step}:")
        print("  Observation:", record["obs"])
        print("  Action:", record["action"])
        print("  Result:", record["result"])
        print()

if __name__ == "__main__":
    main()
