from cli.colors import Colors


class Banner:

    VERSION = "v0.3.0-alpha"

    @staticmethod
    def show():

        print()

        print(Colors.color("=" * 60, Colors.BRIGHT_CYAN))
        print(Colors.color("                     AI-Team", Colors.BRIGHT_WHITE))
        print(Colors.color("              Multi-Agent AI Framework", Colors.CYAN))
        print(Colors.color("=" * 60, Colors.BRIGHT_CYAN))

        print(
            Colors.color("Version", Colors.BRIGHT_BLUE)
            + f" : {Banner.VERSION}"
        )

        print()

        print(
            Colors.color(
                "Type /help to view available commands.",
                Colors.BRIGHT_BLACK,
            )
        )

        print()
