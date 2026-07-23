from core.agent_role import AgentRole


class AgentRegistry:

    def __init__(self):

        self._agents = {}

    # --------------------------------------------------

    def register(self, agent):

        self._agents[agent.role] = agent

    # --------------------------------------------------

    def get(self, role: AgentRole):

        return self._agents.get(role)

    # --------------------------------------------------

    def exists(self, role: AgentRole):

        return role in self._agents

    # --------------------------------------------------

    def remove(self, role: AgentRole):

        self._agents.pop(role, None)

    # --------------------------------------------------

    def clear(self):

        self._agents.clear()

    # --------------------------------------------------

    def all(self):

        return list(self._agents.values())

    # --------------------------------------------------

    def roles(self):

        return list(self._agents.keys())

    # --------------------------------------------------

    def __len__(self):

        return len(self._agents)


agent_registry = AgentRegistry()
