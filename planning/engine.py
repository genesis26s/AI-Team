from planning.prompt import PLANNING_SYSTEM_PROMPT
from planning.parser import parser
from planning.validator import validator


class PlanningEngine:

    """
    Public interface for AI-Team planning.

    Manager should ONLY call:

        planning_engine.plan(task)

    Nothing else.
    """

    def __init__(self):

        self.system_prompt = PLANNING_SYSTEM_PROMPT

    def plan(self, task):

        raise NotImplementedError(
            "LLM planning has not been connected yet."
        )


planning_engine = PlanningEngine()
