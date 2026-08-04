class Scorer:
    """
    Calculates weighted capability scores for models.
    """

    def score(self, model: dict, weights: dict) -> float:
        """
        Calculate the weighted capability score for a model.

        Parameters
        ----------
        model : dict
            A model profile loaded from model_profiles.json.

        weights : dict
            The capability weight profile.

        Returns
        -------
        float
            Final weighted score (0-100).
        """

        scores = model.get("scores", {})

        total_score = 0.0
        total_weight = 0.0

        for capability, weight in weights.items():

            # Context is stored separately
            if capability == "context":

                context = model.get("context_window", 0)

                if context >= 1_000_000:
                    value = 100
                elif context >= 200_000:
                    value = 90
                elif context >= 128_000:
                    value = 80
                elif context >= 64_000:
                    value = 70
                elif context >= 32_000:
                    value = 60
                else:
                    value = 50

            else:
                value = scores.get(capability, 0)

            total_score += value * weight
            total_weight += weight

        if total_weight == 0:
            return 0.0

        return round(total_score / total_weight, 2)


# Singleton instance
scorer = Scorer()
