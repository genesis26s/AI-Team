import requests

from config import (
    HUGGINGFACE_API_KEY,
    HUGGINGFACE_BASE_URL,
)

from providers.http_provider import HTTPProvider

from core.model import AIModel


class HuggingFaceProvider(HTTPProvider):

    name = "huggingface"

    BASE_URL = HUGGINGFACE_BASE_URL

    API_KEY = HUGGINGFACE_API_KEY

    DEFAULT_MODEL = None

    def available_models(self):

        models = []

        try:

            response = requests.get(

                "https://huggingface.co/api/models",

                headers={
                    "Authorization": f"Bearer {self.API_KEY}"
                },

                params={
                    "limit": 100,
                    "inference": "warm"
                },

                timeout=30,

            )

            response.raise_for_status()

            data = response.json()

            for item in data:

                model_id = item.get("id")

                if not model_id:
                    continue

                tags = item.get("tags", [])

                capabilities = ["chat"]

                lower_tags = [tag.lower() for tag in tags]

                if any("vision" in tag for tag in lower_tags):
                    capabilities.append("vision")

                if any("code" in tag for tag in lower_tags):
                    capabilities.append("coding")

                if any("reason" in tag for tag in lower_tags):
                    capabilities.append("reasoning")

                models.append(

                    AIModel(

                        id=model_id,

                        name=model_id,

                        provider=self.name,

                        free=True,

                        context=None,

                        capabilities=capabilities,

                        description=item.get("description", ""),

                        reasoning="reasoning" in capabilities,

                        coding="coding" in capabilities,

                        vision="vision" in capabilities,

                        metadata=item,

                    )

                )

        except Exception as e:

            print(f"HuggingFace: {e}")

        return models
