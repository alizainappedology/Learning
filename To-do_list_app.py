tasks = []

while True:
    print("\n📋 To-Do List Menu")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
        task = input("Enter a new task: ")
        tasks.append({"task": task, "done": False})
        print("✅ Task added!")

    elif choice == '2':
        print("\n📝 Your Tasks:")
        if not tasks:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {task['task']} [{status}]")

    elif choice == '3':
        task_number = int(input("Enter task number to mark as done: "))
        if 0 < task_number <= len(tasks):
            tasks[task_number - 1]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("Invalid task number.")

    elif choice == '4':
        task_number = int(input("Enter task number to delete: "))
        if 0 < task_number <= len(tasks):
            deleted = tasks.pop(task_number - 1)
            print(f"🗑️ Deleted task: {deleted['task']}")
        else:
            print("Invalid task number.")

    elif choice == '5':
        print("👋 Exiting To-Do List. Goodbye!")
        break

    else:
        print("Invalid option. Please enter a number from 1 to 5.")
