from config import (
    ENABLE_GOOGLE,
    ENABLE_OPENROUTER,
    ENABLE_GITHUB,
    ENABLE_HUGGINGFACE,
)

from providers.google_provider import GoogleProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.github_provider import GitHubProvider
from providers.huggingface_provider import HuggingFaceProvider


class ProviderFactory:

    def __init__(self):

        self.providers = {}

        if ENABLE_OPENROUTER:
            self.providers["openrouter"] = OpenRouterProvider()

        if ENABLE_GITHUB:
            self.providers["github"] = GitHubProvider()

        if ENABLE_HUGGINGFACE:
            self.providers["huggingface"] = HuggingFaceProvider()

        if ENABLE_GOOGLE:
            self.providers["google"] = GoogleProvider()

    # --------------------------------------------------

    def get(self, provider_name: str):

        provider = self.providers.get(provider_name.lower())

        if provider is None:
            raise ValueError(
                f"Unknown or disabled provider: {provider_name}"
            )

        return provider

    # --------------------------------------------------

    def available_providers(self):

        return list(self.providers.keys())

    # --------------------------------------------------

    def all(self):

        return list(self.providers.values())

    # --------------------------------------------------

    def health(self):

        status = {}

        for name, provider in self.providers.items():

            try:
                status[name] = provider.health_check()

            except Exception:
                status[name] = False

        return status


factory = ProviderFactory()
