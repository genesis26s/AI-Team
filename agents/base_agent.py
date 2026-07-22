from services.gateway_service import gateway
from services.agent_config import agent_config

from registry.model_registry import registry

from core.request import AIRequest


class BaseAgent:

    name = "base"

    def chat(
        self,
        prompt,
        system_prompt=None,
    ):

        config = agent_config.get(self.name)

        strategy = config.get("strategy")

        model = registry.best(strategy)

        if model is None:

            raise RuntimeError(
                f"No model available for strategy '{strategy}'."
            )

        request = AIRequest(

            prompt=prompt,

            system_prompt=system_prompt,

            provider=model.provider,

            model=model.id,

            temperature=config.get("temperature", 0.7),

            max_tokens=config.get("max_tokens", 4096),

        )

        return gateway.chat(request)
