import tempfile
import unittest
from pathlib import Path

from models.project import Project
from models.task import Task
from models.user import User
from utils import file_io


class TestFileIO(unittest.TestCase):
    def setUp(self):
        self.original_base = file_io.BASE_DIR
        self.original_data = file_io.FILE_DATA
        self.original_users = file_io.FILE_USERS
        self.original_projects = file_io.FILE_PROJECTS

        self.temp_dir = tempfile.TemporaryDirectory()
        temp_base = Path(self.temp_dir.name)
        file_io.BASE_DIR = temp_base
        file_io.FILE_DATA = temp_base / "data.json"
        file_io.FILE_USERS = temp_base / "users.json"
        file_io.FILE_PROJECTS = temp_base / "projects.json"

    def tearDown(self):
        file_io.BASE_DIR = self.original_base
        file_io.FILE_DATA = self.original_data
        file_io.FILE_USERS = self.original_users
        file_io.FILE_PROJECTS = self.original_projects
        self.temp_dir.cleanup()

    def test_save_and_load_data(self):
        user = User("sam", "sam@mail.com")
        project = Project("Tracker", "CLI", user)
        task = Task("Add command", "Use argparse", "high")
        task.add_contributor("sam")
        project.add_task(task)
        user.add_project(project)

        file_io.save_info([user])
        loaded = file_io.load_data()

        self.assertTrue(file_io.FILE_USERS.exists())
        self.assertTrue(file_io.FILE_PROJECTS.exists())
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].username, "sam")
        self.assertEqual(loaded[0].projects[0].tasks[0].title, "Add command")


if __name__ == "__main__":
    unittest.main()
