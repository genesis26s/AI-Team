class RegistryFilter:
    """
    Filters and searches models inside the registry.
    """

    def free_models(self, registry):

        return registry.get_models()

    def provider_models(self, registry, provider_name):

        return registry.get_models(provider_name)

    def search(self, registry, keyword):

        results = {}

        keyword = keyword.lower()

        for provider, models in registry.get_models().items():

            matches = []

            for model in models:

                if keyword in model.lower():
                    matches.append(model)

            if matches:
                results[provider] = matches

        return results

    def providers(self, registry):

        return list(registry.get_models().keys())

    def total_models(self, registry):

        return registry.model_count()

    def total_providers(self, registry):

        return registry.provider_count()


registry_filter = RegistryFilter()
