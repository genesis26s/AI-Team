from core.agent_role import AgentRole
from core.model_strategy import ModelStrategy
from core.task import Task
from core.request import AIRequest

from registry.model_registry import registry

from services.agent_config import agent_config
from services.gateway_service import gateway


class BaseAgent:

    def __init__(
        self,
        role: AgentRole,
        system_prompt: str = "",
    ):

        self.role = role
        self.system_prompt = system_prompt

    # --------------------------------------------------

    def chat(self, prompt):

        # ----------------------------------------------
        # Agent configuration
        # ----------------------------------------------

        config = agent_config.get(self.role)

        if config is None:

            raise RuntimeError(
                f"No configuration found for {self.role.value}."
            )

        # ----------------------------------------------
        # Select model
        # ----------------------------------------------

        strategy: ModelStrategy = config["strategy"]

        model = registry.best(strategy)

        if model is None:

            raise RuntimeError(
                f"No model found for strategy '{strategy.value}'."
            )

        # ----------------------------------------------
        # Accept either Task or plain text
        # ----------------------------------------------

        if isinstance(prompt, Task):

            prompt_text = prompt.prompt

        else:

            prompt_text = str(prompt)

        # ----------------------------------------------
        # Build request
        # ----------------------------------------------

        request = AIRequest(

            prompt=prompt_text,

            system_prompt=self.system_prompt,

            provider=model.provider,

            model=model.id,

            agent=self.role.value,

            temperature=config.get("temperature", 0.7),

            max_tokens=config.get("max_tokens", 4096),

        )

        # ----------------------------------------------
        # Send request
        # ----------------------------------------------

        return gateway.chat(request)

    # --------------------------------------------------

    @property
    def name(self):

        """
        Backwards compatibility.
        Remove this once every file uses self.role.
        """

        return self.role.value
