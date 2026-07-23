from core.execution_plan import ExecutionPlan


class TaskAnalyzer:

    """
    Uses an LLM to analyze the user's task and
    generate an execution plan.

    IMPORTANT:
    It NEVER answers the user.
    """

    SYSTEM_PROMPT = """
You are the Task Analyzer for AI-Team.

You DO NOT answer the user's request.

Your ONLY job is to analyze it.

Return ONLY valid JSON.

Determine:

- task_type
- confidence
- complexity
- manager_can_answer
- pipeline
- preferred_traits
- notes

Never include markdown.

Never explain.

Output JSON only.
"""

    def analyze(self, task):

        raise NotImplementedError(
            "LLM analysis will be implemented next."
        )


task_analyzer = TaskAnalyzer()
