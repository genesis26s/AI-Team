from abc import ABC, abstractmethod

from core.request import AIRequest
from core.response import AIResponse


class BaseProvider(ABC):
    """
    Base class for every AI provider.

    Every provider MUST inherit from this class.
    """

    name = "base"

    @abstractmethod
    def chat(self, request: AIRequest) -> AIResponse:
        """
        Send a chat request.
        """
        raise NotImplementedError

    @abstractmethod
    def health_check(self) -> bool:
        """
        Return True if provider is available.
        """
        raise NotImplementedError

    @abstractmethod
    def available_models(self) -> list[str]:
        """
        Return supported models.
        """
        raise NotImplementedError
