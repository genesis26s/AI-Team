import json
from pathlib import Path


class ModelRegistry:

    def __init__(self):

        self.models = {}

    def register_provider(self, provider_name):

        if provider_name not in self.models:
            self.models[provider_name] = []

    def register_model(self, provider_name, model):

        self.register_provider(provider_name)

        if model not in self.models[provider_name]:
            self.models[provider_name].append(model)

    def get_models(self, provider_name=None):

        if provider_name is None:
            return self.models

        return self.models.get(provider_name, [])

    def provider_count(self):

        return len(self.models)

    def model_count(self):

        total = 0

        for models in self.models.values():
            total += len(models)

        return total

    def clear(self):

        self.models.clear()

    def save(self, filename="registry/free_models.json"):

        Path(filename).parent.mkdir(parents=True, exist_ok=True)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.models, f, indent=4)

    def load(self, filename="registry/free_models.json"):

        path = Path(filename)

        if not path.exists():
            return

        with open(path, "r", encoding="utf-8") as f:
            self.models = json.load(f)


registry = ModelRegistry()
