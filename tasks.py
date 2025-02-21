from database import load_data, save_data

def add_task(title, description):
    data = load_data()
    task = {
        "id": len(data["tasks"]) + 1,
        "title": title,
        "description": description,
        "completed": False
    }
    data["tasks"].append(task)
    save_data(data)
    print(f"✅ Task '{title}' added successfully!")

def view_tasks():
    data = load_data()
    if not data["tasks"]:
        print("❌ No tasks available.")
    else:
        print("\n📝 Task List:")
        for task in data["tasks"]:
            status = "✅ Completed" if task["completed"] else "❌ Pending"
            print(f"{task['id']}. {task['title']} - {task['description']} ({status})")

def update_task(task_id, new_title, new_description):
    data = load_data()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["title"] = new_title
            task["description"] = new_description
            save_data(data)
            print(f"✏ Task {task_id} updated successfully!")
            return
    print("❌ Task not found!")

def delete_task(task_id):
    data = load_data()
    data["tasks"] = [task for task in data["tasks"] if task["id"] != task_id]
    save_data(data)
    print(f"🗑 Task {task_id} deleted successfully!")

def mark_task_completed(task_id):
    data = load_data()
    for task in data["tasks"]:
        if task["id"] == task_id:
            task["completed"] = True
            save_data(data)
            print(f"✅ Task {task_id} marked as completed!")
            return
    print("❌ Task not found!")
