import json

data_file_path = "data.json"

# Load data from the file when the program starts
try:
    with open(data_file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    # Handle the case where the file doesn't exist yet
    data = {"users": {}, "tasks": []}

logged_in_user = None

def saveData():
    with open(data_file_path, 'w') as file:
        json.dump(data, file)

def register():
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    # For a real-world application, you should hash the password before storing it
    data["users"][username] = {"password": password}
    saveData()

def login():
    global logged_in_user
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in data["users"] and data["users"][username]["password"] == password:
        logged_in_user = username
        print("Login successful!")
    else:
        print("Invalid credentials. Please try again.")

def addTask():
    if logged_in_user is None:
        print("Please login first.")
        return
    task = input("Please enter a task: ")
    data["tasks"].append({"user": logged_in_user, "task": task})
    print(f"Task '{task}' added to the list.")
    saveData()

def listTasks():
    if logged_in_user is None:
        print("Please login first.")
        return
    user_tasks = [task["task"] for task in data["tasks"] if task["user"] == logged_in_user]
    if not user_tasks:
        print("You have no tasks currently.")
    else:
        print("Your tasks: ")
        for index, task in enumerate(user_tasks):
            print(f"Task #{index}. {task}")

if __name__ == "__main__":
    # create a loop to run the app
    print("Welcome to the to-do list app")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("___________________________________________")
        print("1. Register a new user")
        print("2. Login")
        print("3. Add a new task")
        print("4. List tasks")
        print("5. Save and Quit")

        choice = input("Please enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            addTask()
        elif choice == "4":
            listTasks()
        elif choice == "5":
            # Save data to the file before quitting
            saveData()
            break
        else:
            print("Invalid input. Please try again.")

    print("\nGoodbye...")