from pymongo import MongoClient
from bson.objectid import ObjectId

# MongoDB connection
uri = "mongodb://localhost:27017/"
client = MongoClient(uri)

# Database and collection
db = client.todo_db
task_collection = db.tasks

# Insert function
def create_task(description):
    task = {
        'task': description
    }
    result = task_collection.insert_one(task)
    print(f'Task Created with ID: {result.inserted_id}')

# View tasks function
def view_tasks():
    tasks = task_collection.find()
    print("\nYour Tasks:")
    for task in tasks:
        print(f"- {task['task']} (ID: {task['_id']})")

# Delete task function
def delete_task(task_id):
    try:
        result = task_collection.delete_one({'_id': ObjectId(task_id)})
        if result.deleted_count:
            print("Task deleted successfully.")
        else:
            print("No task found with that ID.")
    except Exception as e:
        print("Invalid ID format.")

def update_task(task_id, new_description):
        try:
            result = task_collection.update_one(
                {'_id': ObjectId(task_id)},
                {'$set': {'task': new_description}}
            )
            if result.matched_count:
                print("Task updated successfully.")
            else:
                print("No task found with that ID.")
        except Exception:
            print("Invalid ID format.")

# Menu loop
while True:
    print("\n1. Create Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Update Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        description = input("Enter your Task: ")
        create_task(description)
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        view_tasks()  # Show tasks to help user choose which to delete
        task_id = input("Enter the ID of the task to delete: ")
        delete_task(task_id)
    elif choice == '4':
        view_tasks()
        task_id = input("Enter the ID of the task to update: ")
        new_description = input("Enter the new task description: ")
        update_task(task_id, new_description)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Provide a valid option.")
