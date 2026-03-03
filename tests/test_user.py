#test file for user class



import unittest

from models.project import Project
from models.user import User


class TestUser(unittest.TestCase):
    def test_add_and_find_project(self):
        user = User("alex", "alex@mail.com")
        project = Project("CLI Tool", "Summative", user)

        user.add_project(project)

        self.assertEqual(user.find_project("CLI Tool"), project)
        self.assertEqual(len(user.projects), 1)


if __name__ == "__main__":
    unittest.main()
