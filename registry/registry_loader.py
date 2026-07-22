from providers.provider_factory import factory
from registry.model_registry import registry

from core.model import AIModel


class RegistryLoader:
    """
    Loads every provider's models into the registry.
    """

    def load(self):

        registry.clear()

        providers = factory.available_providers()

        print(f"Found {len(providers)} providers.\n")

        for provider_name in providers:

            print(f"Loading {provider_name}...")

            try:

                provider = factory.get(provider_name)

                # Register the provider OBJECT
                registry.register_provider(provider)

                models = provider.available_models()

                if not models:

                    print("  No models found.\n")
                    continue

                loaded = 0

                for model in models:

                    if isinstance(model, AIModel):

                        # Register the AIModel only
                        registry.register_model(model)

                        loaded += 1

                print(f"  Loaded {loaded} model(s).\n")

            except Exception as e:

                print(f"  Failed: {e}\n")

        return registry

    def reload(self):

        return self.load()


loader = RegistryLoader()
