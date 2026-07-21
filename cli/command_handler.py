from registry.model_registry import registry
from registry.registry_filter import registry_filter


class CommandHandler:
    """
    Handles all CLI commands.
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

            case "agents":
                self.agents()

            case "health":
                self.health()

            case "diagnostics":
                self.diagnostics()

            case "clear":
                self.clear()

            case "version":
                self.version()

            case _:
                print(f"Unknown command: /{command}")

    def help(self):

        print("\n========== Commands ==========")

        print("/help              Show this menu")
        print("/providers         List providers")
        print("/models            Show all models")
        print("/free-models       Show free models")
        print("/agents            List AI agents")
        print("/health            System health")
        print("/diagnostics       Run diagnostics")
        print("/version           Show version")
        print("/clear             Clear terminal")
        print("/exit              Exit AI-Team")

        print()

    def providers(self):

        print("\n========== Providers ==========\n")

        providers = registry_filter.providers(registry)

        if not providers:
            print("No providers loaded.\n")
            return

        for provider in providers:
            print(f"• {provider}")

        print()

    def models(self):

        print("\n========== Models ==========\n")

        models = registry.get_models()

        if not models:
            print("No models loaded.\n")
            return

        for provider, provider_models in models.items():

            print(provider)

            for model in provider_models:
                print(f"   • {model}")

            print()

    def free_models(self):

        print("\n========== Free Models ==========\n")

        self.models()

    def agents(self):

        print("\n========== Agents ==========\n")

        print("🧠 Manager")
        print("📋 Planner")
        print("💻 Developer")
        print("🔍 Reviewer")
        print("⚡ Optimizer")

        print()

    def health(self):

        print("\n========== Health ==========\n")

        print("Registry : OK")
        print(f"Providers: {registry.provider_count()}")
        print(f"Models   : {registry.model_count()}")

        print()

    def diagnostics(self):

        print("\n========== Diagnostics ==========\n")

        print(f"Providers Loaded : {registry.provider_count()}")
        print(f"Models Loaded    : {registry.model_count()}")

        print()

    def version(self):

        print("\nAI-Team v0.3.0-alpha\n")

    def clear(self):

        import os

        os.system("cls" if os.name == "nt" else "clear")


handler = CommandHandler()
