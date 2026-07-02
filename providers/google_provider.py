from google import genai

from config import GOOGLE_API_KEY

from core.request import AIRequest
from core.response import AIResponse


class GoogleProvider:

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
            provider="google",
            model=request.model,
        )