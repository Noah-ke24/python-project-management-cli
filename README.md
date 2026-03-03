# Project Management CLI Tool
A Python CLI app for managing users, projects, and tasks.

## What it does
- Create and list users
- Add projects to users
- Add tasks to projects
- Mark tasks as complete
- Save everything to JSON files

## Setup
#Requirements

- Python 3.10 

### Installation
cd python-project-management-cli
pip install -r requirements.txt
```

## Usage
### Add a user

```bash
python main.py add-user --name "Alice" --email "alice@example.com"
```

### List all users

```bash
python main.py list-users
```

### Add a project

```bash
python main.py add-project --user "Alice" --title "CLI Tool" --description "Build a project management tool" --due-date "2024-12-31"
```

### List projects

```bash
python main.py list-projects
```

### List projects for one user

```bash
python main.py list-projects --user "Alice"
```

### Add a task

```bash
python main.py add-task --project "CLI Tool" --title "Implement add-task command" --assigned-to "Alice"
```

### List tasks

```bash
python main.py list-tasks --project "CLI Tool"
```

### Mark task as complete

```bash
python main.py complete-task --task-id 1
```

## Run tests

```bash
pytest
pytest -v
```

## Project structure

```text
python-project-management-cli/
├── main.py
├── models/
│   ├── user.py
│   ├── project.py
│   └── task.py
├── utils/
│   └── file_handler.py
├── data/
│   └── data.json
├── tests/
│   ├── test_user.py
│   ├── test_project.py
│   ├── test_task.py
│   └── test_file_handler.py
├── requirements.txt
└── README.md
```

## Data storage

Data is saved as JSON in the `data/` folder.

## Known issues

- Task IDs are global (not per project)
- No duplicate-user check yet
- Email format not validated yet

## Future ideas

- Add login system
- Task priorities
- Search feature
- Export to CSV

## Author

**Noah** — Software Engineer