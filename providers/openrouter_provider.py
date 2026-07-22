import requests

from config import (
    OPENROUTER_API_KEY,
    OPENROUTER_BASE_URL,
)

from providers.http_provider import HTTPProvider

from core.model import AIModel


class OpenRouterProvider(HTTPProvider):

    name = "openrouter"

    BASE_URL = OPENROUTER_BASE_URL

    API_KEY = OPENROUTER_API_KEY

    # Default fallback model for OpenRouter.
    DEFAULT_MODEL = "nvidia/nemotron-3-ultra"

    def headers(self):

        headers = super().headers()

        # Optional but recommended by OpenRouter.
        headers["HTTP-Referer"] = "https://github.com/genesis26s/AI-Team"
        headers["X-Title"] = "AI-Team"

        return headers

    # --------------------------------------------------

    def available_models(self):

        models = []

        try:

            response = requests.get(
                "https://openrouter.ai/api/v1/models",
                timeout=30,
            )

            response.raise_for_status()

            data = response.json()

            for item in data.get("data", []):

                model_id = item.get("id")

                if not model_id:
                    continue

                pricing = item.get("pricing", {})

                # Only keep completely free models.
                if (
                    pricing.get("prompt") != "0"
                    or pricing.get("completion") != "0"
                ):
                    continue

                capabilities = ["chat"]

                lower = model_id.lower()

                if any(word in lower for word in [
                    "coder",
                    "code",
                    "programming",
                    "dev"
                ]):
                    capabilities.append("coding")

                if any(word in lower for word in [
                    "reason",
                    "think",
                    "r1",
                    "o1",
                    "o3"
                ]):
                    capabilities.append("reasoning")

                if any(word in lower for word in [
                    "vision",
                    "vl",
                    "image"
                ]):
                    capabilities.append("vision")

                models.append(

                    AIModel(

                        id=model_id,

                        name=item.get("name", model_id),

                        provider=self.name,

                        free=True,

                        context=item.get("context_length"),

                        capabilities=capabilities,

                        description=item.get("description", ""),

                        reasoning="reasoning" in capabilities,

                        coding="coding" in capabilities,

                        vision="vision" in capabilities,

                        input_cost=float(pricing.get("prompt", 0)),

                        output_cost=float(pricing.get("completion", 0)),

                        metadata=item,

                    )

                )

        except Exception as e:

            print(f"OpenRouter: {e}")

        return models
