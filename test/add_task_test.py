import unittest
from mock import patch, MagicMock
from add_task import AddTask
from user_repository import UserRepository
from task_repository import TaskRepository
from user import User
from task import Task
from datetime import datetime

YESTERDAY = datetime(2016, 2, 8)
TODAY = datetime(2016, 2, 9)
TOMORROW = datetime(2016, 2, 10)
LAST_WEEK = datetime(2016, 2, 2)
NEXT_WEEK = datetime(2016, 2, 16)
LAST_MONTH = datetime(2016, 01, 9)
NEXT_MONTH = datetime(2016, 03, 9)


class AddTaskTest(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()
        self.task_repo = TaskRepository()

    def test_add_task_should_deliver_error_if_user_is_not_found(self):
        self.user_repo.find_one = MagicMock(return_value=None)
        add_task = AddTask(self.user_repo, self.task_repo)

        response = add_task({'user': 126})

        self.assertEqual('fail', response['status'])

    @patch('task.datetime')
    def test_should_add_new_task_to_user_task_list_and_return_scheduled_task_list(self, mock_dt):
        request = {
            'user': 126,
            'code': 'add_task',
            'data': {
                'title': 'New Task',
            }
        }
        mock_dt.now.return_value = TODAY
        self.user_repo.find_one = MagicMock(return_value=User(id=1))
        self.task_repo.tasks_for = MagicMock(return_value=[Task(**request['data'])])
        add_task = AddTask(self.user_repo, self.task_repo)

        response = add_task(request)

        self.assertEqual('success', response['status'])
        self.assertEqual([{
            'title': 'New Task',
            'active': True,
            'creation': '2016-02-09 00:00:00'
        }], response['data'])

