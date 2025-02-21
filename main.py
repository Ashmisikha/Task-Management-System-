from tasks import add_task, view_tasks, update_task, delete_task, mark_task_completed

def main():
    while True:
        print("\n📌 Task Management System")
        print("1️⃣ Add Task")
        print("2️⃣ View Tasks")
        print("3️⃣ Update Task")
        print("4️⃣ Delete Task")
        print("5️⃣ Mark Task as Completed")
        print("6️⃣ Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Task Title: ")
            description = input("Task Description: ")
            add_task(title, description)

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            task_id = int(input("Task ID: "))
            new_title = input("New Title: ")
            new_description = input("New Description: ")
            update_task(task_id, new_title, new_description)

        elif choice == "4":
            task_id = int(input("Task ID to Delete: "))
            delete_task(task_id)

        elif choice == "5":
            task_id = int(input("Task ID to Mark as Completed: "))
            mark_task_completed(task_id)

        elif choice == "6":
            print("🚀 Exiting program...")
            break

        else:
            print("❌ Invalid choice! Try again.")

if __name__ == "__main__":
    main()
