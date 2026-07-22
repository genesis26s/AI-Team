import json


class AgentConfig:

    def __init__(self):

        self.reload()

    # ---------------------------------------------

    def reload(self):

        with open("config/agents.json", "r") as file:

            self.config = json.load(file)

    # ---------------------------------------------

    def get(self, name):

        return self.config.get(name.lower(), {})


agent_config = AgentConfig()
