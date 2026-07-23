from core.agent_role import AgentRole

from agents.base_agent import BaseAgent

from services.router import router
from services.pipeline_builder import pipeline_builder
from services.pipeline_executor import pipeline_executor


class Manager(BaseAgent):

    def __init__(self):

        super().__init__(

            role=AgentRole.MANAGER,

            system_prompt="""
You are the Manager of AI-Team.

AI-Team is a collaborative multi-agent AI framework.

Your responsibility is to understand the user's request,
coordinate specialist agents,
and produce the best possible response.

Never perform specialist work yourself unless the task is
simple enough to answer directly.

Always minimize unnecessary API calls.

Think like an orchestration engine.
"""

        )

    # --------------------------------------------------

    def delegate(self, task, registry):

        print("\n🧠 Manager")
        print("Analyzing task...")

        # ------------------------------------------
        # Classify task
        # ------------------------------------------

        task_type = router.classify(task)

        print(f"Task Type : {task_type.value}")

        # ------------------------------------------
        # Build pipeline
        # ------------------------------------------

        pipeline = pipeline_builder.build(task_type)

        # ------------------------------------------
        # No pipeline needed
        # ------------------------------------------

        if not pipeline:

            print("No specialist pipeline required.\n")

            return self.chat(task)

        print("Pipeline:")

        for role in pipeline:

            print(f" • {role.value}")

        print()

        # ------------------------------------------
        # Execute pipeline
        # ------------------------------------------

        return pipeline_executor.execute(

            task=task,

            pipeline=pipeline,

            registry=registry,

        )
