from cli.console import console

from services.agent_registry import agent_registry

from registry.registry_loader import loader

from agents.manager import Manager
from agents.developer import Developer
from agents.reviewer import Reviewer
from agents.optimizer import Optimizer


def initialize():

    print("Initializing AI-Team...\n")

    # -----------------------------
    # Register Agents
    # -----------------------------

    agent_registry.register(Manager())
    agent_registry.register(Developer())
    agent_registry.register(Reviewer())
    agent_registry.register(Optimizer())

    print(f"Registered {len(agent_registry)} agent(s).")

    # -----------------------------
    # Load Models
    # -----------------------------

    loader.load()

    print("Initialization complete.\n")


def main():

    initialize()

    console.start()


if __name__ == "__main__":

    main()
