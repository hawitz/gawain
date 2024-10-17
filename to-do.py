# To-do List Application

# Initialize an empty list to hold the tasks
todo_list = []

# Function to display the current to-do list
def show_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. {task['description']} [{status}]")
    print()

# Function to add a task to the list
def add_task():
    task_desc = input("Enter the task description: ")
    todo_list.append({"description": task_desc, "completed": False})
    print(f"Task '{task_desc}' added.\n")

# Function to mark a task as completed
def complete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print(f"Task {task_num} marked as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Function to delete a task from the list
def delete_task():
    show_tasks()
    if not todo_list:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['description']}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

# Main loop for the application
def main():
    while True:
        print("To-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            complete_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice, please choose a valid option.\n")

# Run the application
if __name__ == "__main__":
    main()
