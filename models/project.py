from dataclasses import dataclass, field

from models.task import Task


@dataclass
class Project:
    name: str
    description: str
    owner: object
    tasks: list = field(default_factory=list)

    def add_task(self, task):
        self.tasks.append(task)

    def find_task(self, title):
        for task in self.tasks:
            if task.title == title:
                return task
        return None

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "tasks": [task.to_dict() for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data, owner):
        project = cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            owner=owner,
        )
        project.tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]
        return project
