from cli.colors import Colors


class HelpMenu:
    """
    Displays the AI-Team CLI help menu.
    """

    @staticmethod
    def show():

        print()

        print(Colors.color("=" * 60, Colors.BRIGHT_CYAN))
        print(Colors.color("                 AI-Team CLI Help", Colors.BRIGHT_WHITE))
        print(Colors.color("=" * 60, Colors.BRIGHT_CYAN))

        commands = [

            ("/help", "Show this help menu"),
            ("/providers", "List available providers"),
            ("/models", "Show discovered models"),
            ("/free-models", "Show verified free models"),
            ("/agents", "List all AI agents"),
            ("/health", "Show system health"),
            ("/diagnostics", "Run diagnostics"),
            ("/version", "Show AI-Team version"),
            ("/clear", "Clear the terminal"),
            ("/exit", "Exit AI-Team")

        ]

        for command, description in commands:

            print(
                Colors.color(f"{command:<20}", Colors.BRIGHT_GREEN)
                + description
            )

        print()
