from core.execution_plan import ExecutionPlan
from core.task_complexity import TaskComplexity
from core.agent_role import AgentRole


class PlanningValidationError(Exception):
    pass


class PlanningValidator:

    """
    Validates an ExecutionPlan before it
    is executed.
    """

    def validate(self, plan: ExecutionPlan) -> ExecutionPlan:

        # -----------------------------
        # Confidence
        # -----------------------------

        if not 0 <= plan.confidence <= 100:
            raise PlanningValidationError(
                "Confidence must be between 0 and 100."
            )

        # -----------------------------
        # Complexity
        # -----------------------------

        if not isinstance(
            plan.complexity,
            TaskComplexity,
        ):
            raise PlanningValidationError(
                "Invalid task complexity."
            )

        # -----------------------------
        # Pipeline
        # -----------------------------

        for role in plan.pipeline:

            if not isinstance(role, AgentRole):

                raise PlanningValidationError(
                    f"Invalid agent role: {role}"
                )

        # -----------------------------
        # Traits
        # -----------------------------

        for name, value in plan.preferred_traits.items():

            if not isinstance(value, int):

                raise PlanningValidationError(
                    f"{name} must be an integer."
                )

            if value < 0 or value > 100:

                raise PlanningValidationError(
                    f"{name} must be between 0 and 100."
                )

        return plan


validator = PlanningValidator()
