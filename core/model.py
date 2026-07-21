from dataclasses import dataclass, field


@dataclass
class AIModel:
    """
    Represents a model discovered from a provider.
    """

    id: str
    name: str
    provider: str

    free: bool = True

    context: int | None = None

    capabilities: list[str] = field(default_factory=list)

    description: str = ""

    input_cost: float = 0.0
    output_cost: float = 0.0

    vision: bool = False

    reasoning: bool = False

    coding: bool = False

    metadata: dict = field(default_factory=dict)
