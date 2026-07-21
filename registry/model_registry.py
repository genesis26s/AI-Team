from core.model import AIModel


class ModelRegistry:
    """
    Stores every discovered model from every provider.
    """

    def __init__(self):

        self.providers = set()

        self.models = {}

    # --------------------------------------------------

    def clear(self):

        self.providers.clear()
        self.models.clear()

    # --------------------------------------------------

    def register_provider(self, provider: str):

        self.providers.add(provider)

        self.models.setdefault(provider, [])

    # --------------------------------------------------

    def register_model(
        self,
        provider: str,
        model: AIModel
    ):

        self.models.setdefault(provider, [])

        self.models[provider].append(model)

    # --------------------------------------------------

    def get_models(self):

        return self.models

    # --------------------------------------------------

    def get_provider_models(
        self,
        provider: str
    ):

        return self.models.get(provider, [])

    # --------------------------------------------------

    def provider_count(self):

        return len(self.providers)

    # --------------------------------------------------

    def model_count(self):

        return sum(
            len(models)
            for models in self.models.values()
        )

    # --------------------------------------------------

    def all_models(self):

        models = []

        for provider_models in self.models.values():

            models.extend(provider_models)

        return models

    # --------------------------------------------------

    def free_models(self):

        return [
            model
            for model in self.all_models()
            if model.free
        ]

    # --------------------------------------------------

    def coding_models(self):

        return [
            model
            for model in self.all_models()
            if model.coding
        ]

    # --------------------------------------------------

    def reasoning_models(self):

        return [
            model
            for model in self.all_models()
            if model.reasoning
        ]

    # --------------------------------------------------

    def vision_models(self):

        return [
            model
            for model in self.all_models()
            if model.vision
        ]


registry = ModelRegistry()
