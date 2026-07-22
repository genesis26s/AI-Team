from services.gateway_service import gateway
from services.agent_config import agent_config

from registry.model_registry import registry

from core.request import AIRequest
from core.task import Task


class BaseAgent:

    def __init__(
        self,
        name,
        system_prompt=""
    ):

        self.name = name.lower()
        self.system_prompt = system_prompt

    # --------------------------------------------------

    def chat(self, prompt):

        config = agent_config.get(self.name)

        strategy = config.get("strategy")

        model = registry.best(strategy)

        if model is None:

            raise RuntimeError(
                f"No model found for strategy '{strategy}'."
            )

        # ----------------------------------------------
        # Accept either a Task object or plain text
        # ----------------------------------------------

        if isinstance(prompt, Task):

            prompt_text = prompt.prompt

        else:

            prompt_text = str(prompt)

        # ----------------------------------------------

        request = AIRequest(

            prompt=prompt_text,

            system_prompt=self.system_prompt,

            provider=model.provider,

            model=model.id,

            temperature=config.get("temperature", 0.7),

            max_tokens=config.get("max_tokens", 4096),

        )

        return gateway.chat(request)
