import uuid
from datetime import datetime


class Task:

    def __init__(self, prompt: str):

        self.id = str(uuid.uuid4())

        self.prompt = prompt

        self.created_at = datetime.now()

        self.status = "pending"

        self.plan = ""

        self.assigned_agents = []

        self.developer_output = ""

        self.reviewer_output = ""

        self.optimizer_output = ""

        self.final_output = ""

        self.logs = []

    def log(self, message: str):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.logs.append(f"[{timestamp}] {message}")

    def __str__(self):

        return (
            f"Task(id={self.id}, "
            f"status={self.status}, "
            f"prompt={self.prompt})"
        )