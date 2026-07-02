from dataclasses import dataclass
from typing import Optional


@dataclass
class AIRequest:
    prompt: str
    provider: str
    model: str

    agent: Optional[str] = None
    system_prompt: Optional[str] = None

    temperature: float = 0.7
    max_tokens: int = 4096

    priority: int = 1