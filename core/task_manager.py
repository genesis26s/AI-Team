from core.task import Task


class TaskManager:

    def create_task(self, prompt: str):

        return Task(prompt)