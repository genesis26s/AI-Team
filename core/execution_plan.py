from dataclasses import dataclass, field
from typing import Dict, List

from core.agent_role import AgentRole
from core.task_complexity import TaskComplexity


@dataclass(frozen=True)
class ExecutionPlan:

    # ==========================================
    # Task Information
    # ==========================================

    task_type: str

    intent: str

    confidence: int

    complexity: TaskComplexity

    manager_can_answer: bool

    # ==========================================
    # Execution
    # ==========================================

    pipeline: List[AgentRole] = field(default_factory=list)

    # ==========================================
    # Model Selection
    # ==========================================

    preferred_traits: Dict[str, int] = field(default_factory=dict)

    # ==========================================
    # Metadata
    # ==========================================

    estimated_steps: int = 0

    notes: str = ""

    # ==========================================
    # Helpers
    # ==========================================

    @property
    def requires_pipeline(self) -> bool:

        return len(self.pipeline) > 0

    @property
    def pipeline_names(self) -> List[str]:

        return [agent.value for agent in self.pipeline]

    def summary(self) -> dict:

        return {

            "task_type": self.task_type,

            "intent": self.intent,

            "confidence": self.confidence,

            "complexity": self.complexity.value,

            "manager_can_answer": self.manager_can_answer,

            "pipeline": self.pipeline_names,

            "preferred_traits": self.preferred_traits,

            "estimated_steps": self.estimated_steps,

            "notes": self.notes,

        }

    def __str__(self):

        return (
            f"ExecutionPlan("
            f"task_type={self.task_type}, "
            f"intent={self.intent}, "
            f"complexity={self.complexity.value}, "
            f"confidence={self.confidence}, "
            f"pipeline={self.pipeline_names})"
        )
