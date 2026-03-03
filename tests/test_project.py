import unittest

from models.project import Project
from models.task import Task
from models.user import User


class TestProject(unittest.TestCase):
    def test_add_and_find_task(self):
        user = User("alex", "alex@mail.com")
        project = Project("CLI Tool", "Summative", user)
        task = Task("Implement parser", "argparse", "high")

        project.add_task(task)

        self.assertEqual(project.find_task("Implement parser"), task)
        self.assertEqual(len(project.tasks), 1)


if __name__ == "__main__":
    unittest.main()