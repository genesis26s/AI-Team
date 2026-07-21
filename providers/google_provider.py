from google import genai

from config import GOOGLE_API_KEY

from providers.base_provider import BaseProvider

from core.request import AIRequest
from core.response import AIResponse
from core.model import AIModel


class GoogleProvider(BaseProvider):

    name = "google"

    DEFAULT_MODEL = "gemini-2.5-flash"

    def __init__(self):

        self.client = genai.Client(
            api_key=GOOGLE_API_KEY
        )

    # --------------------------------------------------

    def chat(self, request: AIRequest):

        try:

            response = self.client.models.generate_content(
                model=request.model or self.DEFAULT_MODEL,
                contents=request.prompt,
            )

            return AIResponse(
                success=True,
                text=response.text,
                provider=self.name,
                model=request.model or self.DEFAULT_MODEL,
            )

        except Exception as e:

            return AIResponse(
                success=False,
                text=str(e),
                provider=self.name,
                model=request.model or self.DEFAULT_MODEL,
            )

    # --------------------------------------------------

    def available_models(self):

        models = []

        try:

            for model in self.client.models.list():

                model_name = model.name.replace("models/", "")

                models.append(

                    AIModel(

                        id=model_name,

                        name=model.display_name or model_name,

                        provider=self.name,

                        free=True,

                        context=getattr(
                            model,
                            "input_token_limit",
                            None,
                        ),

                        capabilities=["chat"],

                        reasoning="gemini" in model_name.lower(),

                        coding="gemini" in model_name.lower(),

                        vision="vision" in model_name.lower()
                        or "image" in model_name.lower(),

                        description=getattr(
                            model,
                            "description",
                            "",
                        ),

                    )

                )

        except Exception as e:

            print(f"Google: {e}")

        return models

    # --------------------------------------------------

    def health_check(self):

        try:

            self.client.models.list()

            return True

        except Exception:

            return False
