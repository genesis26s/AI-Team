from core.model import AIModel


class ModelRegistry:

    def __init__(self):

        self.models = []
        self.providers = {}

    # ==================================================
    # Providers
    # ==================================================

    def register_provider(self, provider):

        self.providers[provider.name.lower()] = provider

    # --------------------------------------------------

    def get_provider(self, name):

        return self.providers.get(name.lower())

    # --------------------------------------------------

    def get_providers(self):

        return list(self.providers.values())

    # --------------------------------------------------

    def provider_names(self):

        return list(self.providers.keys())

    # --------------------------------------------------

    def provider_count(self):

        return len(self.providers)

    # ==================================================
    # Models
    # ==================================================

    def register(self, model: AIModel):

        self.models.append(model)

    # --------------------------------------------------

    def register_model(self, model: AIModel):

        self.register(model)

    # --------------------------------------------------

    def clear(self):

        self.models.clear()

    # --------------------------------------------------

    def clear_models(self):

        self.models.clear()

    # --------------------------------------------------

    def get_models(self):

        return self.models

    # --------------------------------------------------

    def all(self):

        return self.models

    # --------------------------------------------------

    def model_count(self):

        return len(self.models)

    # --------------------------------------------------

    def find(self, model_id):

        for model in self.models:

            if model.id == model_id:

                return model

        return None

    # --------------------------------------------------

    def filter(self, **kwargs):

        results = self.models

        for key, value in kwargs.items():

            results = [

                model

                for model in results

                if getattr(model, key, None) == value

            ]

        return results

    # ==================================================
    # Strategy Selection
    # ==================================================

    def best(self, strategy):

        strategy = strategy.lower()

        if strategy == "best_coding":

            models = self.filter(coding=True)

        elif strategy == "best_reasoning":

            models = self.filter(reasoning=True)

        elif strategy == "best_vision":

            models = self.filter(vision=True)

        elif strategy == "best_chat":

            models = self.models

        else:

            models = self.models

        if not models:

            return None

        models.sort(

            key=lambda model: (

                not getattr(model, "free", True),

                -(getattr(model, "context", 0) or 0),

                getattr(model, "name", "").lower(),

            )

        )

        return models[0]

    # --------------------------------------------------

    def best_coding(self):

        return self.best("best_coding")

    # --------------------------------------------------

    def best_reasoning(self):

        return self.best("best_reasoning")

    # --------------------------------------------------

    def best_vision(self):

        return self.best("best_vision")

    # --------------------------------------------------

    def best_chat(self):

        return self.best("best_chat")

    # ==================================================
    # Statistics
    # ==================================================

    def stats(self):

        return {

            "providers": self.provider_count(),

            "models": self.model_count(),

        }


registry = ModelRegistry()
