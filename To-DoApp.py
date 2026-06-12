import os

tasks = "tasks.txt"

def load_tasks():
    if not os.path.exists(tasks):
        return []
    with open(tasks, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(tasks, "w") as f:
        for task in tasks:
            f.write(task+"\n")

def complete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        choice = int(input("Enter the task number to complete."))
        if 0 < choice <= len(tasks):
            if tasks[choice-1].startwith("[ ]"):
                tasks[choice-1] = tasks[choice-1].replace("[ ]", "[x]", 1)
                save_tasks(tasks)
                print("Task completed")
            else:
                print("Invalid choice")
    except ValueError:
        print("Enter a valid number")


def add_task(tasks):
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task)
        save_tasks(tasks)
        print("Task added")
    else:
         print("Invalid task")

def view_tasks(tasks):
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input("Enter the task number."))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            save_tasks(tasks)
            print("Task deleted")
        else:
            print("Invalid choice")


def main():
    while True:
        print("Welcome to To-Do App")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Complete task")
        print("5. Exit")

        choice = int(input("Enter your choice."))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            delete_task(tasks)
        elif choice == 4:
            complete_task(tasks)
        elif choice == 5:
            print("Thank you for using the To-Do App")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
