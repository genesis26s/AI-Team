from cli.banner import Banner
from cli.parser import parser
from cli.command_handler import handler

from services.agent_registry import agent_registry

from core.agent_role import AgentRole
from core.task import Task


class Console:
    """
    AI-Team interactive console.
    """

    def __init__(self):
        pass

    # --------------------------------------------------

    def get_manager(self):

        manager = registry.get(AgentRole.MANAGER)

        if manager is None:

            raise RuntimeError(
                "Manager agent is not registered."
            )

        return manager

    # --------------------------------------------------

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

                # ------------------------------------------
                # Commands
                # ------------------------------------------

                if parsed["type"] == "command":

                    handler.execute(

                        parsed["command"],

                        parsed["args"],

                    )

                    continue

                # ------------------------------------------
                # Build Task
                # ------------------------------------------

                task = Task(

                    prompt=parsed["input"]

                )

                # ------------------------------------------
                # Get current manager
                # ------------------------------------------

                manager = self.get_manager()

                # ------------------------------------------
                # Delegate
                # ------------------------------------------

                response = manager.delegate(

                    task,

                    registry,

                )

                # ------------------------------------------
                # Output
                # ------------------------------------------

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
