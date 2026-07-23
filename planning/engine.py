from planning.prompt import PLANNING_SYSTEM_PROMPT
from planning.parser import parser
from planning.validator import validator

from services.gateway_service import gateway
from registry.model_registry import registry

from core.request import AIRequest
from core.model_strategy import ModelStrategy


class PlanningEngine:

    """
    Generates an ExecutionPlan using an LLM.
    """

    def __init__(self):

        self.system_prompt = PLANNING_SYSTEM_PROMPT

    # --------------------------------------------------

    def plan(self, task):

        # -----------------------------
        # Select planning model
        # -----------------------------

        model = registry.best(ModelStrategy.PLANNING)

        if model is None:

            raise RuntimeError(
                "No planning model available."
            )

        # -----------------------------
        # Build request
        # -----------------------------

        request = AIRequest(

            prompt=task.prompt,

            provider=model.provider,

            model=model.id,

            system_prompt=self.system_prompt,

            temperature=0.2,

            max_tokens=1200,

        )

        # -----------------------------
        # Call gateway
        # -----------------------------

        response = gateway.chat(request)

        if not response.success:

            raise RuntimeError(response.text)

        # -----------------------------
        # Parse JSON
        # -----------------------------

        plan = parser.parse(response.text)

        # -----------------------------
        # Validate
        # -----------------------------

        validator.validate(plan)

        return plan


planning_engine = PlanningEngine()
