from providers.google_provider import GoogleProvider
from providers.openrouter_provider import OpenRouterProvider
from providers.cerebras_provider import CerebrasProvider


class ProviderFactory:

    _providers = {
        "google": GoogleProvider,
        "openrouter": OpenRouterProvider,
        "cerebras": CerebrasProvider,
    }

    @classmethod
    def create(cls, provider_name: str):

        provider_name = provider_name.lower()

        if provider_name not in cls._providers:
            raise ValueError(
                f"Unknown provider '{provider_name}'. "
                f"Available providers: {list(cls._providers.keys())}"
            )

        return cls._providers[provider_name]()

    @classmethod
    def register(cls, name, provider):
        cls._providers[name.lower()] = provider

    @classmethod
    def available(cls):
        return list(cls._providers.keys())
