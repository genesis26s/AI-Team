import json
from pathlib import Path

from registry.model_registry import registry


class RegistryCache:
    """
    Handles saving and loading the local model registry cache.
    """

    CACHE_FILE = "registry/free_models.json"

    def save(self):

        Path(self.CACHE_FILE).parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.CACHE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                registry.get_models(),
                file,
                indent=4
            )

    def load(self):

        path = Path(self.CACHE_FILE)

        if not path.exists():
            return False

        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            registry.models = json.load(file)

        return True

    def clear(self):

        path = Path(self.CACHE_FILE)

        if path.exists():
            path.unlink()

        registry.clear()

    def exists(self):

        return Path(self.CACHE_FILE).exists()


cache = RegistryCache()
