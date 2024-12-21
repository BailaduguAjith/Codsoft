class ToDoList:
    def __init__(self):
        self.tasks = {}

    def create_task(self):
        task_name = input("Enter task name: ")
        task_description = input("Enter task description: ")
        self.tasks[task_name] = {"description": task_description, "completed": False}
        print("Task created successfully!")

    def update_task(self):
        task_name = input("Enter task name: ")
        if task_name in self.tasks:
            task_description = input("Enter new task description: ")
            self.tasks[task_name]["description"] = task_description
            print("Task updated successfully!")
        else:
            print("Task not found!")

    def delete_task(self):
        task_name = input("Enter task name: ")
        if task_name in self.tasks:
            del self.tasks[task_name]
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    def view_tasks(self):
        for task_name, task_details in self.tasks.items():
            status = "Completed" if task_details["completed"] else "Pending"
            print(f"Task Name: {task_name}")
            print(f"Task Description: {task_details['description']}")
            print(f"Task Status: {status}")
            print("------------------------")

    def mark_task_completed(self):
        task_name = input("Enter task name: ")
        if task_name in self.tasks:
            self.tasks[task_name]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Task not found!")

def main():
    todo_list = ToDoList()

    while True:
        print("1. Create Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Mark Task Completed")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            todo_list.create_task()
        elif choice == "2":
            todo_list.update_task()
        elif choice == "3":
            todo_list.delete_task()
        elif choice == "4":
            todo_list.view_tasks()
        elif choice == "5":
            todo_list.mark_task_completed()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


