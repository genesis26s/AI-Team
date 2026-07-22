from agents.base_agent import BaseAgent


class Manager(BaseAgent):

    def __init__(self):

        super().__init__(

            name="manager",

            system_prompt="""
You are the Manager of AI-Team.

AI-Team is a collaborative multi-agent AI framework.

Your responsibility is to understand the user's request,
coordinate specialist agents, combine their work, and produce
one polished final response.

You are responsible for:

• Understanding the task
• Delegating work efficiently
• Avoiding unnecessary API calls
• Combining results
• Ensuring the final answer is complete

Never attempt specialist work yourself unless it is extremely
simple.

Always think like a technical project manager rather than a
general AI assistant.

Your goal is to maximize answer quality while minimizing
execution cost and latency.
"""

        )

    # --------------------------------------------------

    def delegate(self, task, registry):

        print("\n🧠 Manager")
        print("Planning task...")

        developer = registry.get("developer")
        reviewer = registry.get("reviewer")
        optimizer = registry.get("optimizer")

        # ----------------------------
        # Developer
        # ----------------------------

        dev_response = developer.chat(task)

        print("✓ Developer finished")

        if not dev_response.success:
            return dev_response

        # ----------------------------
        # Reviewer
        # ----------------------------

        review_response = reviewer.chat(dev_response.text)

        print("✓ Reviewer finished")

        if not review_response.success:
            return review_response

        # ----------------------------
        # Optimizer
        # ----------------------------

        optimized_response = optimizer.chat(review_response.text)

        print("✓ Optimizer finished")

        return optimized_response
