tasks = "tasks.txt"

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

