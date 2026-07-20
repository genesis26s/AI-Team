from google import genai

from config import GOOGLE_API_KEY

from core.request import AIRequest
from core.response import AIResponse

from providers.base_provider import BaseProvider


class GoogleProvider(BaseProvider):

    name = "google"

    def __init__(self):
        self.client = genai.Client(api_key=GOOGLE_API_KEY)

    def chat(self, request: AIRequest):

        prompt = request.prompt

        if request.system_prompt:
            prompt = (
                f"System Instructions:\n"
                f"{request.system_prompt}\n\n"
                f"User Request:\n"
                f"{request.prompt}"
            )

        response = self.client.models.generate_content(
            model=request.model,
            contents=prompt,
        )

        return AIResponse(
            success=True,
            text=response.text,
            provider=self.name,
            model=request.model,
        )

    def health_check(self):
        return GOOGLE_API_KEY is not None

    def available_models(self):
        return [
            "gemini-2.5-flash",
            "gemini-2.5-pro",
        ]
