from core.task_type import TaskType


class PipelineBuilder:

    """
    Builds the execution pipeline for a given task type.

    The router decides WHAT the task is.
    The pipeline builder decides WHICH agents should execute it.
    """

    def __init__(self):

        self.pipelines = {

            # -----------------------------
            # Greetings
            # -----------------------------

            TaskType.GREETING: [],

            # -----------------------------
            # Normal conversations
            # -----------------------------

            TaskType.CHAT: [],

            # -----------------------------
            # Coding
            # -----------------------------

            TaskType.CODING: [

                "planner",

                "developer",

                "reviewer",

                "optimizer",

            ],

            # -----------------------------
            # Debugging
            # -----------------------------

            TaskType.DEBUGGING: [

                "planner",

                "developer",

                "reviewer",

                "optimizer",

            ],

            # -----------------------------
            # Research
            # -----------------------------

            TaskType.RESEARCH: [

                "researcher",

                "writer",

            ],

            # -----------------------------
            # Writing
            # -----------------------------

            TaskType.WRITING: [

                "writer",

                "reviewer",

            ],

            # -----------------------------
            # Mathematics
            # -----------------------------

            TaskType.MATH: [

                "researcher",

                "reviewer",

            ],

            # -----------------------------
            # Vision
            # -----------------------------

            TaskType.VISION: [

                "designer",

            ],

            # -----------------------------
            # File Generation
            # -----------------------------

            TaskType.FILE: [

                "planner",

                "developer",

                "reviewer",

                "optimizer",

                "packager",

            ],

            # -----------------------------
            # Unknown
            # -----------------------------

            TaskType.UNKNOWN: [],

        }

    # --------------------------------------------------

    def build(self, task_type: TaskType):

        return self.pipelines.get(task_type, []).copy()

    # --------------------------------------------------

    def register_pipeline(self, task_type: TaskType, agents: list):

        self.pipelines[task_type] = agents.copy()

    # --------------------------------------------------

    def add_agent(self, task_type: TaskType, agent: str):

        self.pipelines.setdefault(task_type, [])

        if agent not in self.pipelines[task_type]:

            self.pipelines[task_type].append(agent)

    # --------------------------------------------------

    def remove_agent(self, task_type: TaskType, agent: str):

        if task_type in self.pipelines:

            if agent in self.pipelines[task_type]:

                self.pipelines[task_type].remove(agent)

    # --------------------------------------------------

    def all(self):

        return self.pipelines.copy()


pipeline_builder = PipelineBuilder()
