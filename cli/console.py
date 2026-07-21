from cli.banner import Banner
from cli.parser import parser
from cli.command_handler import handler

from services.agent_registry import registry

from core.task import Task


class Console:
    """
    AI-Team interactive console.
    """

    def __init__(self):

        self.manager = registry.get("manager")

    def start(self):

        Banner.show()

        while True:

            try:

                user_input = input("You > ").strip()

                if not user_input:
                    continue

                if user_input.lower() in ("exit", "/exit"):
                    print("\nGoodbye!\n")
                    break

                parsed = parser.parse(user_input)

                if parsed["type"] == "command":

                    handler.execute(
                        parsed["command"],
                        parsed["args"]
                    )

                    continue

                task = Task(
                    prompt=parsed["input"]
                )

                response = self.manager.delegate(
                    task,
                    registry
                )

                print()
                print("=" * 50)
                print("FINAL RESPONSE")
                print("=" * 50)
                print()

                print(response)

                print()

            except KeyboardInterrupt:

                print("\n\nGoodbye!\n")
                break

            except Exception as e:

                print(f"\nError: {e}\n")


console = Console()
