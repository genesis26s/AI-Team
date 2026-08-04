class Scorer:
    """
    Calculates weighted capability scores for models.
    """

    def score(self, model: dict, weights: dict) -> float:
        """
        Calculate a weighted score.

        Parameters
        ----------
        model : dict
            Model profile loaded from model_profiles.json

        weights : dict
            Weight profile loaded from capability_weights.json

        Returns
        -------
        float
            Final weighted score.
        """

        scores = model.get("scores", {})

        total = 0.0

        for capability, weight in weights.items():

            # Context
