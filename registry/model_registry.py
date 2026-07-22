from core.model import AIModel


class ModelRegistry:

    def __init__(self):

        self.models = []

    # --------------------------------------------------

    def register(self, model: AIModel):

        self.models.append(model)

    # --------------------------------------------------

    def clear(self):

        self.models.clear()

    # --------------------------------------------------

    def all(self):

        return self.models

    # --------------------------------------------------

    def providers(self):

        return sorted(
            list(
                {
                    model.provider
                    for model in self.models
                }
            )
        )

    # --------------------------------------------------

    def provider_count(self):

        return len(self.providers())

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

    # --------------------------------------------------

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

                not model.free,

                -(model.context or 0),

                model.name.lower(),

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


registry = ModelRegistry()
