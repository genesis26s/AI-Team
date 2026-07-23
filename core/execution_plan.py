from dataclasses import dataclass, field
from typing import Dict, List

from core.agent_role import AgentRole
from core.task_complexity import TaskComplexity


@dataclass
class ExecutionPlan:

    # ==========================================
    # Task Information
    # ==========================================

    task_type: str

    confidence: int

    complexity: TaskComplexity

    manager_can_answer: bool

    # ==========================================
    # Execution
    # ==========================================

    pipeline: List[AgentRole] = field(default_factory=list)

    # ==========================================
    # Model Preferences
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
    def requires_pipeline(self):

        return len(self.pipeline) > 0

    def summary(self):

        return {

            "task_type": self.task_type,

            "confidence": self.confidence,

            "complexity": self.complexity.value,

            "manager_can_answer": self.manager_can_answer,

            "pipeline": [

                role.value

                for role in self.pipeline

            ],

            "preferred_traits": self.preferred_traits,

            "estimated_steps": self.estimated_steps,

            "notes": self.notes,

        }
