from providers.provider_factory import ProviderFactory

from core.request import AIRequest


class Gateway:

    def chat(self, request: AIRequest):

        provider = ProviderFactory.create(request.provider)

        return provider.chat(request)
