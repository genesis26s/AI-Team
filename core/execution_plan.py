from dataclasses import dataclass, field
from typing import List, Dict

from core.agent_role import AgentRole


@dataclass
class ExecutionPlan:

    # ----------------------------
    # Task Analysis
    # ----------------------------

    task_type: str

    confidence: int

    complexity: str

    manager_can_answer: bool

    # ----------------------------
    # Execution
    # ----------------------------

    pipeline: List[AgentRole] = field(default_factory=list)

    # ----------------------------
    # Model Selection
    # ----------------------------

    preferred_traits: Dict[str, int] = field(default_factory=dict)

    # ----------------------------
    # Metadata
    # ----------------------------

    notes: str = ""

    estimated_steps: int = 0
