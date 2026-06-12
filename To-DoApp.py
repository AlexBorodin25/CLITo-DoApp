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

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added")

def view_task():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")

def delete_task():
    if len(tasks) == 0:
        print("No tasks")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        choice = int(input("Enter the task number."))
        if 0 < choice <= len(tasks):
            del tasks[choice-1]
            print("Task deleted")
        else:
            print("Invalid choice")

def main():
    while True:
        print("Welcome to To-Do App")
        print("1. Add task")
        print("2. View task")
        print("3. Delete task")
        print("4. Exit")

        choice = int(input("Enter your choice."))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            delete_task()
        elif choice == 4:
            print("Thank you for using the To-Do App")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
