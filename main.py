from services.agent_registry import registry
from core.task_manager import TaskManager

manager = registry.get("manager")
task_manager = TaskManager()

print("=" * 50)
print("              AI TEAM")
print("=" * 50)
print("Type 'exit' to quit.")

while True:

    prompt = input("\nYou > ").strip()

    if prompt.lower() == "exit":
        print("\nGoodbye!")
        break

    if not prompt:
        continue

    # Create a new task
    task = task_manager.create_task(prompt)

    # Let the Manager handle the task
    response = manager.delegate(task, registry)

    print("\n" + "=" * 50)
    print("FINAL RESPONSE")
    print("=" * 50)
    print()

    print(response.text)

    print("\n" + "=" * 50)
    print("TASK INFO")
    print("=" * 50)
    print(f"Task ID : {task.id}")
    print(f"Status  : {task.status}")

    if task.logs:
        print("\nLogs:")
        for log in task.logs:
            print(f"• {log}")