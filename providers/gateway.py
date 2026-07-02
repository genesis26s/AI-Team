from providers.google_provider import GoogleProvider

from core.request import AIRequest


class Gateway:

    def __init__(self):

        self.providers = {}

        self.register(
            "google",
            GoogleProvider()
        )

    def register(self, name, provider):
        self.providers[name] = provider

    def chat(self, request: AIRequest):

        provider = self.providers.get(request.provider)

        if provider is None:
            raise Exception(f"Provider '{request.provider}' not found.")

        return provider.chat(request)