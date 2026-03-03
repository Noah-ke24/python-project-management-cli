import unittest

from models.task import Task


class TestTask(unittest.TestCase):
    def test_complete_and_contributors(self):
        task = Task("Build", "Create feature", "medium")

        task.add_contributor("alex")
        task.add_contributor("alex")
        task.complete()

        self.assertTrue(task.completed)
        self.assertEqual(task.contributors, ["alex"])


if __name__ == "__main__":
    unittest.main()
