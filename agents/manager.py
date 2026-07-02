from agents.base_agent import BaseAgent


class Manager(BaseAgent):

    def __init__(self):

        super().__init__(
            name="Manager",
            system_prompt="""
You are the Project Manager of an AI software team.

You NEVER write production code yourself.

Your job is to:
- Understand the user's request.
- Decide which specialist agents should perform the work.
- Coordinate the work.
- Produce the final response.

Available agents:
- Developer
- Reviewer
- Optimizer
"""
        )

    def delegate(self, prompt: str, registry):

        text = prompt.lower()

        # Greetings
        if any(word in text for word in [
            "hello", "hi", "hey", "how are you"
        ]):
            return self.chat(prompt)

        # Review tasks
        if any(word in text for word in [
            "review", "bug", "debug", "fix"
        ]):
            reviewer = registry.get("reviewer")
            return reviewer.chat(prompt)

        # Optimization tasks
        if any(word in text for word in [
            "optimize", "optimise", "performance"
        ]):
            optimizer = registry.get("optimizer")
            return optimizer.chat(prompt)

        # Default workflow
        developer = registry.get("developer")
        reviewer = registry.get("reviewer")
        optimizer = registry.get("optimizer")

        print("\n🧠 Manager")
        print("Planning task...")

        dev = developer.chat(prompt)
        print("✔ Developer finished")

        review = reviewer.chat(
            f"Review this solution:\n\n{dev.text}"
        )
        print("✔ Reviewer finished")

        optimized = optimizer.chat(
            f"""
Improve this solution while preserving functionality.

Original user request:
{prompt}

Developer solution:
{dev.text}

Reviewer feedback:
{review.text}
"""
        )
        print("✔ Optimizer finished")

        return optimized