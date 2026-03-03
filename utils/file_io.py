
# utils and file I/O functions    just tought myself how to do this.
import json
from pathlib import Path

from models.project import Project
from models.user import User

BASE_DIR = Path(__file__).resolve().parent.parent / "data"
FILE_DATA = BASE_DIR / "data.json"
FILE_USERS = BASE_DIR / "users.json"
FILE_PROJECTS = BASE_DIR / "projects.json"


def save_data(users, _projects=None):
    save_info(users)


def save_info(users):
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    full_data = [user.to_dict() for user in users]
    users_data = [{"username": user.username, "email": user.email} for user in users]
    projects_data = []

    for user in users:
        for project in user.projects:
            projects_data.append(
                {
                    "owner": user.username,
                    "name": project.name,
                    "description": project.description,
                    "task_count": len(project.tasks),
                }
            )

    _write_json(FILE_DATA, full_data)
    _write_json(FILE_USERS, users_data)
    _write_json(FILE_PROJECTS, projects_data)


def load_data():
    try:
        data = _read_json(FILE_DATA)
        users = []
        for user_data in data:
            user = User(user_data.get("username", ""), user_data.get("email", ""))
            user.projects = [
                Project.from_dict(project_data, user)
                for project_data in user_data.get("projects", [])
            ]
            users.append(user)
        projects = [project for user in users for project in user.projects]
        return users, projects
    except (FileNotFoundError, json.JSONDecodeError, TypeError, KeyError):
        return [], []


def _write_json(path, payload):
    with open(path, "w", encoding="utf-8") as file:
        json.dump(payload, file, indent=2)


def _read_json(path):
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)
