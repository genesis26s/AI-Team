from agents.manager import Manager
from agents.developer import Developer
from agents.reviewer import Reviewer
from agents.optimizer import Optimizer


class AgentRegistry:

    def __init__(self):

        self.agents = {
            "manager": Manager(),
            "developer": Developer(),
            "reviewer": Reviewer(),
            "optimizer": Optimizer(),
        }

    def get(self, name: str):

        agent = self.agents.get(name.lower())

        if agent is None:
            raise ValueError(f"Unknown agent: {name}")

        return agent


registry = AgentRegistry()