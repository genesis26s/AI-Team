from services.capability_engine import capability_engine
from services.scorer import scorer


class ModelSelector:
    """
    Selects the best model for an agent based on
    weighted capability scoring.
    """

    def __init__(self):
        capability_engine.load()

    def reload(self):
        capability_engine.reload()

    def select(
        self,
        profile: str = "global",
        provider: str | None = None,
        free_only: bool = True
    ):
        """
        Select the highest scoring model.

        Parameters
        ----------
        profile : str
            Capability profile to use
            (developer, planner, reviewer...)

        provider : str | None
            Optional provider filter.

        free_only : bool
            Ignore paid models.
        """

        weights = capability_engine.get_weights(profile)

        best_model = None
        best_score = -1

        for model in capability_engine.get_models():

            # Skip paid models
            if free_only and not model.get("free", True):
                continue

            # Provider filter
            if provider is not None:
                if model.get("provider") != provider:
                    continue

            score = scorer.score(model, weights)

            if score > best_score:
                best_score = score
                best_model = model

        return best_model

    def top_models(
        self,
        profile: str = "global",
        limit: int = 5
    ):
        """
        Return the top scoring models.
        """

        weights = capability_engine.get_weights(profile)

        ranked = []

        for model in capability_engine.get_models():

            score = scorer.score(model, weights)

            ranked.append((score, model))

        ranked.sort(
            key=lambda item: item[0],
            reverse=True
        )

        return ranked[:limit]


# Singleton
model_selector = ModelSelector()
