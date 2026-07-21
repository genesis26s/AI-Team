from providers.google_provider import GoogleProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.github_provider import GitHubProvider
from providers.huggingface_provider import HuggingFaceProvider


class ProviderFactory:

    def __init__(self):

        self.providers = {
            "google": GoogleProvider(),
            "openrouter": OpenRouterProvider(),
            "github": GitHubProvider(),
            "huggingface": HuggingFaceProvider(),
        }

    def get(self, provider_name: str):

        provider = self.providers.get(provider_name.lower())

        if provider is None:
            raise ValueError(f"Unknown provider: {provider_name}")

        return provider

    def available_providers(self):

        return list(self.providers.keys())

    def health(self):

        status = {}

        for name, provider in self.providers.items():
            status[name] = provider.health_check()

        return status


factory = ProviderFactory()
