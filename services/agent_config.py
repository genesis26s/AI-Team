from core.agent_role import AgentRole
from core.model_strategy import ModelStrategy


class AgentConfig:

    def __init__(self):

        self.config = {

            AgentRole.MANAGER: {

                "strategy": ModelStrategy.REASONING,

                "temperature": 0.4,

                "max_tokens": 4096,

            },

            AgentRole.PLANNER: {

                "strategy": ModelStrategy.REASONING,

                "temperature": 0.3,

                "max_tokens": 4096,

            },

            AgentRole.DEVELOPER: {

                "strategy": ModelStrategy.CODING,

                "temperature": 0.2,

                "max_tokens": 8192,

            },

            AgentRole.REVIEWER: {

                "strategy": ModelStrategy.REASONING,

                "temperature": 0.2,

                "max_tokens": 4096,

            },

            AgentRole.OPTIMIZER: {

                "strategy": ModelStrategy.CODING,

                "temperature": 0.1,

                "max_tokens": 4096,

            },

            AgentRole.RESEARCHER: {

                "strategy": ModelStrategy.REASONING,

                "temperature": 0.3,

                "max_tokens": 8192,

            },

            AgentRole.WRITER: {

                "strategy": ModelStrategy.WRITING,

                "temperature": 0.6,

                "max_tokens": 8192,

            },

            AgentRole.DESIGNER: {

                "strategy": ModelStrategy.VISION,

                "temperature": 0.4,

                "max_tokens": 4096,

            },

            AgentRole.MARKETER: {

                "strategy": ModelStrategy.WRITING,

                "temperature": 0.7,

                "max_tokens": 8192,

            },

            AgentRole.PACKAGER: {

                "strategy": ModelStrategy.CODING,

                "temperature": 0.1,

                "max_tokens": 4096,

            },

        }

    # --------------------------------------------------

    def get(self, role: AgentRole):

        return self.config.get(role)

    # --------------------------------------------------

    def register(self, role: AgentRole, config: dict):

        self.config[role] = config

    # --------------------------------------------------

    def update(self, role: AgentRole, **kwargs):

        if role not in self.config:

            self.config[role] = {}

        self.config[role].update(kwargs)

    # --------------------------------------------------

    def all(self):

        return self.config.copy()


agent_config = AgentConfig()
