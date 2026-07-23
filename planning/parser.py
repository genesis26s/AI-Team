import json

from core.execution_plan import ExecutionPlan
from core.task_complexity import TaskComplexity
from core.agent_role import AgentRole


class PlanningParser:

    """
    Converts the Planning Engine's JSON output
    into a strongly-typed ExecutionPlan.
    """

    def parse(self, raw: str) -> ExecutionPlan:

        data = json.loads(raw)

        pipeline = []

        for agent in data.get("pipeline", []):

            pipeline.append(
                AgentRole(agent.lower())
            )

        complexity = TaskComplexity(
            data["complexity"].lower()
        )

        return ExecutionPlan(

            task_type=data["task_type"],

            intent=data["intent"],

            confidence=int(data["confidence"]),

            complexity=complexity,

            manager_can_answer=bool(
                data["manager_can_answer"]
            ),

            pipeline=pipeline,

            preferred_traits=data.get(
                "preferred_traits",
                {},
            ),

            estimated_steps=len(pipeline),

            notes=data.get(
                "notes",
                "",
            ),

        )


parser = PlanningParser()
