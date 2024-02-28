def show_menu():
    print("Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")


def add_task(todo_list):
    task = input("Enter the task: ")
    todo_list[len(todo_list) + 1] = {"task": task, "done": False}
    print("Task added successfully!")


def view_tasks(todo_list):
    if len(todo_list) == 0:
        print("No tasks in the list.")
    else:
        print("Tasks:")
        for task_id, task_info in todo_list.items():
            print(f"{task_id}. {'[Done]' if task_info['done'] else '[Pending]'} {task_info['task']}")


def mark_task_as_done(todo_list):
    task_id = int(input("Enter the task ID to mark as done: "))
    if task_id in todo_list:
        todo_list[task_id]['done'] = True
        print("Task marked as done.")
    else:
        print("Task ID not found.")


def delete_task(todo_list):
    task_id = int(input("Enter the task ID to delete: "))
    if task_id in todo_list:
        del todo_list[task_id]
        print("Task deleted successfully.")
    else:
        print("Task ID not found.")


def main():
    todo_list = {}
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_task_as_done(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
