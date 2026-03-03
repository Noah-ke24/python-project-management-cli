from models.project import Project
from models.task import Task
from models.user import User
from utils import file_io


def find_user(users, name):
    for user in users:
        if user.username == name:
            return user
    return None


def find_project(users, name):
    for user in users:
        for project in user.projects:
            if project.name == name:
                return project
    return None


def find_task(users, title):
    for user in users:
        for project in user.projects:
            for task in project.tasks:
                if task.title == title:
                    return task
    return None


def add_user():
    users, _ = file_io.load_data()
    name = input("Name: ")
    email = input("Email: ")
    users.append(User(name, email))
    file_io.save_data(users, [])
    print("User added!")


def list_users():
    users, _ = file_io.load_data()
    for user in users:
        print(f"- {user.username} ({user.email})")


def add_project():
    users, _ = file_io.load_data()
    user_name = input("Username: ")
    title = input("Project title: ")
    user = find_user(users, user_name)
    if user:
        user.add_project(Project(title, "", user))
        file_io.save_data(users, [])
        print("Project added!")
    else:
        print("User not found")


def list_projects():
    users, _ = file_io.load_data()
    user_name = input("Username: ")
    user = find_user(users, user_name)
    if user:
        for project in user.projects:
            print(f"- {project.name}")
    else:
        print("User not found")


def add_task():
    users, _ = file_io.load_data()
    project_name = input("Project: ")
    title = input("Task title: ")
    project = find_project(users, project_name)
    if project:
        project.add_task(Task(title, "", "medium"))
        file_io.save_data(users, [])
        print("Task added!")
    else:
        print("Project not found")


def complete_task():
    users, _ = file_io.load_data()
    title = input("Task title: ")
    task = find_task(users, title)
    if task:
        task.complete()
        file_io.save_data(users, [])
        print("Task completed!")
    else:
        print("Task not found")


def main():
    while True:
        print("\n1. Add User")
        print("2. List Users")
        print("3. Add Project")
        print("4. List Projects")
        print("5. Add Task")
        print("6. Complete Task")
        print("7. Exit")
        
        choice = input("\nChoose: ")
        
        if choice == "1":
            add_user()
        elif choice == "2":
            list_users()
        elif choice == "3":
            add_project()
        elif choice == "4":
            list_projects()
        elif choice == "5":
            add_task()
        elif choice == "6":
            complete_task()
        elif choice == "7":
            break


if __name__ == "__main__":
    main()