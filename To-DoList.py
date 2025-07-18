FILENAME = "tasks.txt"
def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return [task.strip() for task in file.readlines()]
    except FileNotFoundError:
        return []
def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")
def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        print("Task added.")
    else:
        print("Empty task not added.")
def remove_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            print(f"Task '{tasks.pop(index)}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
def main():
    tasks = load_tasks()
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved.")
            break
        else:
            print("Invalid option. Choose 1-4.")

if __name__ == "__main__":
    main()
