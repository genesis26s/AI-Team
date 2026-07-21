from providers.provider_factory import factory
from registry.model_registry import registry


class RegistryLoader:
    """
    Loads models from every provider into the Model Registry.
    """

    def load(self):

        registry.clear()

        for provider_name in factory.available_providers():

            provider = factory.get(provider_name)

            registry.register_provider(provider_name)

            try:

                models = provider.available_models()

                for model in models:
                    registry.register_model(provider_name, model)

            except Exception as e:

                print(f"[Registry] Failed loading {provider_name}: {e}")

        return registry

    def reload(self):

        return self.load()


loader = RegistryLoader()
