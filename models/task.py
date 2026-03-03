from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    description: str
    priority: str
    completed: bool = False
    contributors: list = field(default_factory=list)

    def complete(self):
        self.completed = True

    def add_contributor(self, username):
        if username and username not in self.contributors:
            self.contributors.append(username)

    def remove_contributor(self, username):
        if username in self.contributors:
            self.contributors.remove(username)

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "contributors": self.contributors,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            title=data.get("title", ""),
            description=data.get("description", ""),
            priority=data.get("priority", ""),
            completed=data.get("completed", False),
            contributors=data.get("contributors", []),
        )
