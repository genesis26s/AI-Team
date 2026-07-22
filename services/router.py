from core.task import Task
from core.task_type import TaskType


class Router:

    """
    Responsible ONLY for classifying tasks.
    """

    def classify(self, task: Task) -> TaskType:

        prompt = task.prompt.lower().strip()

        # -----------------------------
        # Greetings
        # -----------------------------

        greetings = {

            "hi",

            "hello",

            "hey",

            "yo",

            "sup",

            "good morning",

            "good afternoon",

            "good evening",

        }

        if prompt in greetings:

            return TaskType.GREETING

        # -----------------------------
        # Coding
        # -----------------------------

        coding_keywords = [

            "python",

            "javascript",

            "java",

            "c#",

            "c++",

            "discord",

            "bug",

            "error",

            "traceback",

            "fix",

            "code",

            "program",

            "script",

            ".py",

            ".js",

            ".html",

            ".css",

        ]

        if any(word in prompt for word in coding_keywords):

            return TaskType.CODING

        # -----------------------------
        # Research
        # -----------------------------

        research_keywords = [

            "what is",

            "who is",

            "where is",

            "when",

            "why",

            "how does",

            "explain",

            "research",

        ]

        if any(word in prompt for word in research_keywords):

            return TaskType.RESEARCH

        # -----------------------------
        # Default
        # -----------------------------

        return TaskType.CHAT


router = Router()
