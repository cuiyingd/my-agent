from my_agent import Agent


def test_agent_runs():
    agent = Agent()
    history = agent.run(max_steps=3)
    assert len(history) >= 1
    assert "action" in history[0]
    assert "result" in history[0]
from my_agent import Agent

def test_agent_runs():
    agent = Agent()
    history = agent.run(max_steps=3)
    assert len(history) >= 1
    assert "action" in history[0]
    assert "result" in history[0]
