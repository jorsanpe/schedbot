import unittest
from mock import patch
from datetime import datetime
from task import Task


class TaskTest(unittest.TestCase):
    def test_task_as_dict(self):
        task = Task(title='a task', start=datetime(2016, 1, 1), creation=datetime(2016, 1, 1))

        self.assertEqual({
            'title': 'a task',
            'start': '2016-01-01 00:00:00',
            'creation': '2016-01-01 00:00:00',
            'active': True,
        }, task.as_dict())

    @patch('task.datetime')
    def test_task_that_has_started_is_active(self, mock_dt):
        task = Task(start=datetime(2016, 1, 1))
        mock_dt.now.return_value = datetime(2016, 2, 2)
        self.assertTrue(task.is_active())

    @patch('task.datetime')
    def test_task_that_has_not_started_is_not_active(self, mock_dt):
        task = Task(start=datetime(2016, 1, 2))
        mock_dt.now.return_value = datetime(2016, 1, 1)
        self.assertFalse(task.is_active())

    @patch('task.datetime')
    def test_task_in_daily_range_is_active(self, mock_dt):
        task = Task(start=datetime(2016, 1, 1),
                    daily={'start': datetime(2016, 1, 1, 8, 0), 'end': datetime(2016, 1, 1, 16, 0)})
        mock_dt.now.return_value = datetime(2016, 2, 2, 10, 0)
        self.assertTrue(task.is_active())

    @patch('task.datetime')
    def test_task_outside_daily_range_is_not_active(self, mock_dt):
        task = Task(start=datetime(2016, 1, 1),
                    daily={'start': datetime(2016, 1, 1, 8, 0), 'end': datetime(2016, 1, 1, 16, 0)})
        mock_dt.now.return_value = datetime(2016, 2, 2, 7, 0)
        self.assertFalse(task.is_active())
        mock_dt.now.return_value = datetime(2016, 2, 2, 17, 0)
        self.assertFalse(task.is_active())
