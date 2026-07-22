from core.agent_role import AgentRole


class PipelineExecutor:

    """
    Executes an agent pipeline.

    Responsible ONLY for running agents
    in the correct order.
    """

    def execute(
        self,
        task,
        pipeline,
        registry,
    ):

        current_input = task

        final_response = None

        for role in pipeline:

            agent = registry.get(role)

            if agent is None:

                print(f"Skipping {role.value} (not registered).")

                continue

            response = agent.chat(current_input)

            print(f"✓ {role.value.title()} finished")

            if not response.success:

                return response

            current_input = response.text

            final_response = response

        return final_response


pipeline_executor = PipelineExecutor()
