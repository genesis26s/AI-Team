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

    def delegate(self, task, registry):

        # Task object -> prompt string
        prompt = task.prompt
        text = prompt.lower()

        task.status = "processing"
        task.log("Manager received task.")

        # Greetings
        if any(word in text for word in [
            "hello", "hi", "hey", "how are you"
        ]):
            response = self.chat(prompt)
            task.final_output = response.text
            task.status = "completed"
            task.log("Handled as a normal conversation.")
            return response

        # Review tasks
        if any(word in text for word in [
            "review", "bug", "debug", "fix"
        ]):
            reviewer = registry.get("reviewer")
            response = reviewer.chat(prompt)

            task.reviewer_output = response.text
            task.final_output = response.text
            task.status = "completed"
            task.log("Sent directly to Reviewer.")

            return response

        # Optimization tasks
        if any(word in text for word in [
            "optimize", "optimise", "performance"
        ]):
            optimizer = registry.get("optimizer")
            response = optimizer.chat(prompt)

            task.optimizer_output = response.text
            task.final_output = response.text
            task.status = "completed"
            task.log("Sent directly to Optimizer.")

            return response

        # Default workflow
        developer = registry.get("developer")
        reviewer = registry.get("reviewer")
        optimizer = registry.get("optimizer")

        print("\n🧠 Manager")
        print("Planning task...")

        dev = developer.chat(prompt)
        task.developer_output = dev.text
        task.log("Developer completed task.")
        print("✔ Developer finished")

        review = reviewer.chat(
            f"Review this solution:\n\n{dev.text}"
        )
        task.reviewer_output = review.text
        task.log("Reviewer completed review.")
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

        task.optimizer_output = optimized.text
        task.final_output = optimized.text
        task.status = "completed"
        task.log("Optimizer completed task.")
        task.log("Task finished successfully.")

        print("✔ Optimizer finished")

        return optimized
