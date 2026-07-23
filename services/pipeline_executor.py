from core.execution_plan import ExecutionPlan

from services.agent_registry import agent_registry


class PipelineExecutor:

    """
    Executes an ExecutionPlan.

    It NEVER decides which agents to use.

    It ONLY executes the pipeline produced
    by the Planning Engine.
    """

    def execute(self, plan: ExecutionPlan, task):

        current_output = task.prompt

        print("\nPipeline")

        if not plan.pipeline:

            print("  (empty)")

            return None

        for role in plan.pipeline:

            print(f"• {role.value.title()}")

            agent = agent_registry.get(role)

            if agent is None:

                raise RuntimeError(

                    f"Agent '{role.value}' is not registered."

                )

            response = agent.chat(current_output)

            if not response.success:

                return response

            current_output = response.text

        return response


pipeline_executor = PipelineExecutor()
