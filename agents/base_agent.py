from services.gateway_service import gateway
from core.request import AIRequest


class BaseAgent:

    def __init__(
        self,
        name: str,
        system_prompt: str,
        provider: str = "google",
        model: str = "gemini-2.5-flash"
    ):

        self.name = name
        self.system_prompt = system_prompt

        self.provider = provider
        self.model = model

        self.gateway = gateway

    def chat(self, prompt: str):

        request = AIRequest(
            prompt=prompt,
            provider=self.provider,
            model=self.model,
            agent=self.name,
            system_prompt=self.system_prompt
        )

        return self.gateway.chat(request)