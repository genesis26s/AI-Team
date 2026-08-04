import json
from pathlib import Path


class CapabilityEngine:
    """
    Loads and manages model capability profiles
    and capability weight profiles.
    """

    def __init__(self):
        self.models = {}
        self.weights = {}

        self._profiles_path = Path("registry/model_profiles.json")
        self._weights_path = Path("config/capability_weights.json")

    def load(self):
        """Load all capability data."""
        self._load_models()
        self._load_weights()

    def reload(self):
        """Reload everything from disk."""
        self.load()

    def _load_models(self):
        if not self._profiles_path.exists():
            self.models = {}
            return

        with open(self._profiles_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        models = data.get("models", [])

        self.models = {
            model["id"]: model
            for model in models
        }

    def _load_weights(self):
        if not self._weights_path.exists():
            self.weights = {}
            return

        with open(self._weights_path, "r", encoding="utf-8") as f:
            self.weights = json.load(f)

    def get_models(self):
        """Return all registered models."""
        return list(self.models.values())

    def get_model(self, model_id: str):
        """Return a single model profile."""
        return self.models.get(model_id)

    def get_profiles(self):
        """Alias for get_models()."""
        return self.get_models()

    def get_weights(self, profile: str = "global"):
        """Return a capability weight profile."""
        return self.weights.get(profile, {})

    def has_model(self, model_id: str):
        return model_id in self.models

    def has_profile(self, profile: str):
        return profile in self.weights


# Singleton instance
capability_engine = CapabilityEngine()
