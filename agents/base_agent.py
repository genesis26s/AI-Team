import json
from pathlib import Path


class ModelRegistry:
    def __init__(self, path: str = "models.json"):
        self.path = Path(path)

        if not self.path.exists():
            raise FileNotFoundError(
                f"Model configuration file not found: {self.path}"
            )

        with open(self.path, "r", encoding="utf-8") as f:
            self.models = json.load(f)

    def get(self, agent_name: str) -> dict:
        agent_name = agent_name.lower()

        if agent_name not in self.models:
            raise ValueError(
                f"No model configuration found for '{agent_name}'."
            )

        return self.models[agent_name]

    def reload(self):
        with open(self.path, "r", encoding="utf-8") as f:
            self.models = json.load(f)

    def agents(self):
        return list(self.models.keys())
