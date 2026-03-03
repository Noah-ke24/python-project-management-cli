from dataclasses import dataclass, field


@dataclass
class User:
    username: str
    email: str
    projects: list = field(default_factory=list)

    def add_project(self, project):
        self.projects.append(project)

    def find_project(self, name):
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email,
            "projects": [project.to_dict() for project in self.projects],
        }
