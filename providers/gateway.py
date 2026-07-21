from providers.provider_factory import factory


class Gateway:

    def chat(self, request):

        provider = factory.get(request.provider)

        return provider.chat(request)


gateway = Gateway()
