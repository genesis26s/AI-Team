import os

from cli.help import HelpMenu

from registry.model_registry import registry
from registry.registry_loader import loader
from registry.registry_cache import cache

from core.version import VERSION


class CommandHandler:
    """
    Handles all AI-Team CLI commands.
    """

    def execute(self, command, args=None):

        if args is None:
            args = []

        match command:

            case "help":
                self.help()

            case "providers":
                self.providers()

            case "models":
                self.models()

            case "free-models":
                self.free_models()

            case "refresh-models":
                self.refresh_models()

            case "agents":
                self.agents()

            case "health":
                self.health()

            case "diagnostics":
                self.diagnostics()

            case "version":
                self.version()

            case "clear":
                self.clear()

            case _:
                print(f"\nUnknown command: /{command}\n")

    # ----------------------------------------

    def help(self):

        HelpMenu.show()

    # ----------------------------------------

    def providers(self):

        print("\n========== Providers ==========\n")

        providers = registry.get_providers()

        if not providers:

            print("No providers loaded.\n")
            return

        for provider in providers:

            print(f"• {provider.name}")

        print()

    # ----------------------------------------

    def models(self):

        print("\n========== Models ==========\n")

        models = registry.get_models()

        if not models:

            print("No models loaded.\n")
            return

        for model in models:

            status = "FREE" if getattr(model, "free", True) else "PAID"

            print(
                f"{model.provider:<14}"
                f"{model.name:<40}"
                f"{status}"
            )

        print()

    # ----------------------------------------

    def free_models(self):

        print("\n========== Free Models ==========\n")

        models = [
            model
            for model in registry.get_models()
            if getattr(model, "free", True)
        ]

        if not models:

            print("No free models loaded.\n")
            return

        for model in models:

            print(
                f"{model.provider:<14}"
                f"{model.name}"
            )

        print()

    # ----------------------------------------

    def refresh_models(self):

        print()
        print("Refreshing Model Registry...\n")

        registry.clear()

        loader.load()

        cache.save()

        print()
        print("Registry updated successfully.")
        print(f"Providers : {registry.provider_count()}")
        print(f"Models    : {registry.model_count()}")
        print()

    # ----------------------------------------

    def agents(self):

        print("\n========== Agents ==========\n")

        print("🧠 Manager")
        print("💻 Developer")
        print("🔍 Reviewer")
        print("⚡ Optimizer")

        print()

    # ----------------------------------------

    def health(self):

        print("\n========== Health ==========\n")

        print("Registry  : OK")
        print(f"Providers : {registry.provider_count()}")
        print(f"Models    : {registry.model_count()}")

        print()

    # ----------------------------------------

    def diagnostics(self):

        print("\n========== Diagnostics ==========\n")

        print(f"Providers Loaded : {registry.provider_count()}")
        print(f"Models Loaded    : {registry.model_count()}")

        print()

    # ----------------------------------------

    def version(self):

        print(f"\nAI-Team {VERSION}\n")

    # ----------------------------------------

    def clear(self):

        os.system("cls" if os.name == "nt" else "clear")


handler = CommandHandler()
