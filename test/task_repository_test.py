import unittest
from task_repository import TaskRepository
from task import Task
from user import User


class TaskRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.task_list = [Task(), Task()]
        self.user_list = [User(id=1), User(id=2)]
        self.task_repository = TaskRepository()

    def test_task_repository_should_assign_unique_id_after_adding_task(self):
        self.task_repository.add_task_for(self.a_user(), self.a_task())

        self.assertTrue(self.a_task()['id'] >= 0)

    def test_task_repository_should_return_task_list(self):
        self.task_repository.add_task_for(self.a_user(), self.a_task())

        task_list = self.task_repository.tasks_for(self.a_user())

        self.assertEqual([self.a_task()], task_list)

    def a_task(self):
        return self.task_list[0]

    def a_user(self):
        return self.user_list[0]

    def test_task_repository_should_maintain_different_task_lists_for_different_users(self):
        self.task_repository.add_task_for(self.a_user(), self.a_task())
        self.task_repository.add_task_for(self.user_list[1], self.task_list[1])

        task_list1 = self.task_repository.tasks_for(self.a_user())
        task_list2 = self.task_repository.tasks_for(self.user_list[1])

        self.assertEqual([self.a_task()], task_list1)
        self.assertEqual([self.task_list[1]], task_list2)
