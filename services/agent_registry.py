from core.agent_role import AgentRole

from agents.manager import Manager
from agents.developer import Developer
from agents.reviewer import Reviewer
from agents.optimizer import Optimizer


class AgentRegistry:

    def __init__(self):

        self.agents = {

            AgentRole.MANAGER: Manager(),

            AgentRole.DEVELOPER: Developer(),

            AgentRole.REVIEWER: Reviewer(),

            AgentRole.OPTIMIZER: Optimizer(),

        }

    # --------------------------------------------------

    def get(self, role: AgentRole):

        return self.agents.get(role)

    # --------------------------------------------------

    def register(self, role: AgentRole, agent):

        self.agents[role] = agent

    # --------------------------------------------------

    def unregister(self, role: AgentRole):

        self.agents.pop(role, None)

    # --------------------------------------------------

    def exists(self, role: AgentRole):

        return role in self.agents

    # --------------------------------------------------

    def roles(self):

        return list(self.agents.keys())

    # --------------------------------------------------

    def all(self):

        return self.agents.copy()

    # --------------------------------------------------

    def count(self):

        return len(self.agents)


registry = AgentRegistry()
