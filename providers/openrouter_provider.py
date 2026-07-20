from providers.base_provider import BaseProvider

from core.request import AIRequest
from core.response import AIResponse


class OpenRouterProvider(BaseProvider):

    name = "openrouter"

    def chat(self, request: AIRequest):

        return AIResponse(
            success=False,
            text="OpenRouter provider has not been implemented yet.",
            provider=self.name,
            model=request.model,
        )

    def health_check(self):
        return True

    def available_models(self):
        return [
            "deepseek/deepseek-chat-v3",
            "qwen/qwen3-coder",
            "meta-llama/llama-3.3-70b-instruct",
        ]
