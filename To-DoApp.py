import os

tasks_file = "tasks.txt"

def load_tasks():
    if not os.path.exists(tasks_file):
        return []
    with open(tasks_file, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(task_list):
    with open(tasks_file, "w") as f:
        for task in task_list:
            f.write(task + "\n")

def complete_task(task_list):
    view_tasks(task_list)

    if not task_list:
        return
    try:
        choice = int(input("Enter the task number to complete."))
        if 0 < choice <= len(task_list):
            if task_list[choice-1].startswith("[ ]"):
                task_list[choice-1] = task_list[choice-1].replace("[ ]", "[x]", 1)
                save_tasks(task_list)
                print("Task completed")
            else:
                print("Task is already completed")
        else:
                print("Invalid choice")
    except ValueError:
        print("Enter a valid number")


def add_task(task_list):
    task = input("Enter new task: ").strip()
    if task:
        task_list.append(f"[ ] {task}")
        save_tasks(task_list)
        print("Task added")
    else:
         print("Invalid task")

def view_tasks(task_list):
    if not task_list:
        print("No tasks")
    else:
        print("To-Do List:")
        for i, task in enumerate(task_list):
            print(f"{i+1}. {task}")

def delete_task(task_list):
    view_tasks(task_list)

    if not task_list:
        return

    try:
        choice = int(input("Enter the task number."))
        if 0 < choice <= len(task_list):
            del task_list[choice-1]
            save_tasks(task_list)
            print("Task deleted")
        else:
            print("Invalid choice")
    except ValueError:
        print("Enter a valid number")

def main():
    task_list = load_tasks()

    while True:
        print("Welcome to To-Do App")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice."))
        except ValueError:
            print("Enter a valid number")
            continue

        if choice == 1:
            add_task(task_list)
        elif choice == 2:
            view_tasks(task_list)
        elif choice == 3:
            delete_task(task_list)
        elif choice == 4:
            complete_task(task_list)
        elif choice == 5:
            print("Thank you for using the To-Do App")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()