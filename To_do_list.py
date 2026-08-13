tasks = []

def show_header():
    print("\n" + "=" * 50)
    print("             📝 TO-DO LIST")
    print("=" * 50)


def view_tasks():
    show_header()

    if len(tasks) == 0:
        print("\n📭 Your To-Do List is empty.")
        print("Add a task to get started!")
        return

    print("\n📋 YOUR TASKS")
    print("-" * 50)

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. ☐ {task}")

    print("-" * 50)
    print(f"📊 Total Tasks: {len(tasks)}")


def add_task():
    show_header()

    task = input("\n✏️ Enter a new task: ").strip()

    if task == "":
        print("\n❌ Task cannot be empty!")
        return

    tasks.append(task)

    print("\n" + "-" * 50)
    print("✅ Task added successfully!")
    print(f"📌 Added Task: {task}")
    print("-" * 50)


def delete_task():
    show_header()

    if len(tasks) == 0:
        print("\n📭 There are no tasks to delete.")
        return

    print("\n📋 YOUR TASKS")
    print("-" * 50)

    for i, task in enumerate(tasks, start=1):
        print(f"{i}. ☐ {task}")

    print("-" * 50)

    try:
        task_number = int(input("🗑️ Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("\n❌ Invalid task number!")
            return

        deleted_task = tasks.pop(task_number - 1)

        print("\n" + "-" * 50)
        print("✅ Task deleted successfully!")
        print(f"🗑️ Deleted Task: {deleted_task}")
        print("-" * 50)

    except ValueError:
        print("\n❌ Please enter a valid number.")


def main():
    while True:
        show_header()

        print("\n📌 MENU")
        print("-" * 30)
        print("1. ➕ Add Task")
        print("2. 👀 View Tasks")
        print("3. 🗑️ Delete Task")
        print("4. 🚪 Exit")
        print("-" * 30)

        choice = input("👉 Enter your choice (1-4): ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            delete_task()

        elif choice == "4":
            print("\n" + "=" * 50)
            print("       Thank you for using To-Do List! 👋")
            print("=" * 50)
            break

        else:
            print("\n❌ Invalid choice! Please select 1 to 4.")

        input("\nPress Enter to continue...")

main()