import requests

from config import (
    GITHUB_API_KEY,
    GITHUB_BASE_URL,
)

from providers.http_provider import HTTPProvider

from core.model import AIModel


class GitHubProvider(HTTPProvider):

    name = "github"

    BASE_URL = GITHUB_BASE_URL

    API_KEY = GITHUB_API_KEY

    # The Manager/Registry should normally provide the model.
    DEFAULT_MODEL = None

    def available_models(self):

        models = []

        try:

            response = requests.get(
                "https://models.github.ai/catalog/models",
                headers={
                    "Authorization": f"Bearer {self.API_KEY}",
                    "Accept": "application/json",
                },
                timeout=30,
            )

            response.raise_for_status()

            data = response.json()

            for item in data:

                model_id = item.get("id")

                if not model_id:
                    continue

                capabilities = []

                tags = item.get("tags", [])

                if "chat" in tags:
                    capabilities.append("chat")

                if "vision" in tags:
                    capabilities.append("vision")

                if "embedding" in tags:
                    capabilities.append("embedding")

                if "reasoning" in tags:
                    capabilities.append("reasoning")

                if "code" in tags:
                    capabilities.append("coding")

                models.append(

                    AIModel(
                        id=model_id,
                        name=item.get("name", model_id),
                        provider=self.name,
                        free=True,
                        context=item.get("context_window"),
                        capabilities=capabilities,
                        description=item.get("description", ""),
                        reasoning="reasoning" in capabilities,
                        coding="coding" in capabilities,
                        vision="vision" in capabilities,
                        metadata=item,
                    )

                )

        except Exception as e:

            print(f"GitHub: {e}")

        return models
