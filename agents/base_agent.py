from services.gateway_service import gateway

from core.request import AIRequest
from core.model_registry import ModelRegistry


class BaseAgent:

    _registry = ModelRegistry()

    def __init__(
        self,
        name: str,
        system_prompt: str
    ):
        self.name = name.lower()
        self.system_prompt = system_prompt

        config = self._registry.get(self.name)

        self.provider = config["provider"]
        self.model = config["model"]

        self.temperature = config.get("temperature", 0.7)
        self.max_tokens = config.get("max_tokens", 4096)

        self.fallbacks = config.get("fallbacks", [])

        self.gateway = gateway

    def chat(self, prompt: str):

        request = AIRequest(
            prompt=prompt,
            provider=self.provider,
            model=self.model,
            agent=self.name,
            system_prompt=self.system_prompt,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
        )

        return self.gateway.chat(request)
