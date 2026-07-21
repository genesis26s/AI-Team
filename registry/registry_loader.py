from providers.provider_factory import factory
from registry.model_registry import registry


class RegistryLoader:
    """
    Loads all available models from every provider into the registry.
    """

    def load(self):

        registry.clear()

        providers = factory.available_providers()

        print(f"Found {len(providers)} providers.\n")

        for provider_name in providers:

            print(f"Loading {provider_name}...")

            try:

                provider = factory.get(provider_name)

                registry.register_provider(provider_name)

                models = provider.available_models()

                if not models:

                    print("  No models found.\n")
                    continue

                for model in models:

                    registry.register_model(
                        provider_name,
                        model
                    )

                print(f"  Loaded {len(models)} model(s).\n")

            except Exception as e:

                print(f"  Failed: {e}\n")

        return registry

    def reload(self):

        return self.load()


loader = RegistryLoader()
