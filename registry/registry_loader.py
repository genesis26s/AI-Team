from providers.provider_factory import factory
from registry.model_registry import registry

from core.model import AIModel


class RegistryLoader:
    """
    Loads every enabled provider's models into the registry.
    """

    def load(self):

        registry.clear()

        providers = factory.available_providers()

        print(f"Found {len(providers)} enabled provider(s).\n")

        total_models = 0

        for provider_name in providers:

            print(f"Loading {provider_name}...")

            try:

                provider = factory.get(provider_name)

                # Register provider
                registry.register_provider(provider)

                models = provider.available_models()

                if not models:

                    print("  No models found.\n")
                    continue

                loaded = 0

                for model in models:

                    if isinstance(model, AIModel):

                        registry.register_model(model)
                        loaded += 1

                total_models += loaded

                print(f"  Loaded {loaded} model(s).\n")

            except Exception as e:

                print(f"  Failed: {e}\n")

        print("=" * 50)
        print("Registry Loaded Successfully")
        print("=" * 50)
        print(f"Providers : {registry.provider_count()}")
        print(f"Models    : {registry.model_count()}")
        print()

        return registry

    # --------------------------------------------------

    def reload(self):

        return self.load()


loader = RegistryLoader()
