from abc import ABC, abstractmethod

from core.request import AIRequest
from core.response import AIResponse


class BaseProvider(ABC):
    """
    Base class for every AI provider.
    """

    name = "base"

    @abstractmethod
    def chat(self, request: AIRequest) -> AIResponse:
        pass

    def health_check(self) -> bool:
        return True

    def available_models(self) -> list[str]:
        return []
