from core.agent_role import AgentRole

from agents.base_agent import BaseAgent


class Optimizer(BaseAgent):

    def __init__(self):

        super().__init__(

            role=AgentRole.OPTIMIZER,

            system_prompt="""
You are the Optimizer of AI-Team.

Your responsibility is to improve solutions.

Focus on:

• Performance
• Simplicity
• Maintainability
• Memory usage
• Scalability

Never change functionality.

Only improve implementation quality.
"""

        )
