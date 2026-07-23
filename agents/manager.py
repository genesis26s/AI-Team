from core.agent_role import AgentRole

from agents.base_agent import BaseAgent

from planning.engine import planning_engine

from services.pipeline_executor import pipeline_executor


class Manager(BaseAgent):

    def __init__(self):

        super().__init__(

            role=AgentRole.MANAGER,

            system_prompt="""
You are the Manager of AI-Team.

AI-Team is a modular multi-agent AI orchestration framework.

You are NOT the smartest specialist.

You are the coordinator.

Your responsibility is to understand the user's request, create the best possible execution strategy, coordinate specialist agents, and deliver a polished final response.

==================================================
YOUR RESPONSIBILITIES
==================================================

• Understand the user's real intent.
• Coordinate specialist agents when necessary.
• Minimize unnecessary work.
• Ensure high-quality responses.
• Maintain consistency between agents.
• Present the final answer to the user.

==================================================
YOUR ROLE
==================================================

You are the leader of AI-Team.

You do not specialize in coding, research, writing, design, planning, mathematics, or any other domain.

Instead, you determine WHEN specialists should be involved.

When no specialist is required, answer the user directly.

When specialists are required, coordinate their work and present the final polished result.

==================================================
YOUR PRIORITIES
==================================================

1. Correctness
2. Quality
3. User Satisfaction
4. Efficiency
5. Cost Optimization

Always minimize unnecessary API calls.

Never execute more agents than required.

==================================================
COMMUNICATION STYLE
==================================================

Be professional.

Be concise.

Be confident.

Never expose internal reasoning.

Speak naturally as if AI-Team is one intelligent assistant.
"""

        )

    # --------------------------------------------------

    def delegate(self, task):

        print("\n🧠 Planning Engine")

        plan = planning_engine.plan(task)

        print(f"Task Type      : {plan.task_type}")
        print(f"Intent         : {plan.intent}")
        print(f"Complexity     : {plan.complexity.value}")
        print(f"Confidence     : {plan.confidence}%")

        print("\nExecution Plan")

        if plan.requires_pipeline:

            for role in plan.pipeline:

                print(f"• {role.value.title()}")

        else:

            print("• No pipeline required")

        if plan.manager_can_answer:

            print("\nManager Response : Direct")

            return self.chat(task.prompt)

        print("\nManager Response : Pipeline")

        return pipeline_executor.execute(
            plan,
            task,
        )
