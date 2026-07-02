from dataclasses import dataclass
from typing import Optional


@dataclass
class AIResponse:
    success: bool
    text: str
    provider: str
    model: str

    error: Optional[str] = None