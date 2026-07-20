from providers.base_provider import BaseProvider

from core.request import AIRequest
from core.response import AIResponse


class CerebrasProvider(BaseProvider):

    name = "cerebras"

    def chat(self, request: AIRequest):

        return AIResponse(
            success=False,
            text="Cerebras provider has not been implemented yet.",
            provider=self.name,
            model=request.model,
        )

    def health_check(self):
        return True

    def available_models(self):
        return [
            "llama-4-scout",
        ]
