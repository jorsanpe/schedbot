import unittest
from mock import patch
from scheduler import Scheduler
from task import Task
from datetime import datetime


class SchedulerTest(unittest.TestCase):
    def test_should_return_empty_task_list_when_empty_task_list_is_passed(self):
        scheduler = Scheduler()
        scheduled = scheduler.schedule([])
        self.assertTrue([] == scheduled)

    def test_should_return_a_one_task_list_when_task_list_contains_single_task(self):
        scheduler = Scheduler()
        task = Task()
        scheduled = scheduler.schedule([task])
        self.assertTrue([task] == scheduled)

    def test_task_with_end_date_prevail_over_task_without_end_date(self):
        scheduler = Scheduler()
        task_with_end = Task(end=datetime(2016, 12, 31))
        task = Task()
        scheduled = scheduler.schedule([task, task_with_end])
        self.assertTrue(scheduled[0] is task_with_end)
        self.assertTrue(scheduled[1] is task)

    def test_task_with_earlier_end_date_prevail_over_task_with_farther_end_date(self):
        scheduler = Scheduler()
        task1 = Task(end=datetime(2016, 1, 31))
        task2 = Task(end=datetime(2016, 2, 28))
        task3 = Task(end=datetime(2015, 12, 31))
        scheduled = scheduler.schedule([task1, task2, task3])
        self.assertTrue(scheduled[0] is task3)
        self.assertTrue(scheduled[1] is task1)
        self.assertTrue(scheduled[2] is task2)

    @patch('task.datetime')
    def test_task_without_start_date_prevails_over_tasks_that_have_not_started(self, mock_dt):
        scheduler = Scheduler()
        task1 = Task(start=datetime(2016, 12, 31))
        task2 = Task(start=datetime(2017, 1, 31))
        task3 = Task()
        mock_dt.now.return_value = datetime(2016, 1, 1)
        scheduled = scheduler.schedule([task1, task2, task3])
        self.assertTrue(scheduled[0] is task3)
        self.assertTrue(scheduled[1] is task1)
        self.assertTrue(scheduled[2] is task2)

    @patch('task.datetime')
    def test_task_that_has_started_prevails_over_task_without_start_date(self, mock_dt):
        scheduler = Scheduler()
        task1 = Task(start=datetime(2016, 1, 31))
        task2 = Task()
        mock_dt.now.return_value = datetime(2016, 2, 1)
        scheduled = scheduler.schedule([task1, task2])
        self.assertTrue(scheduled[0] is task1)
        self.assertTrue(scheduled[1] is task2)

    @patch('task.datetime')
    def test_from_tasks_that_have_started_task_with_earliest_deadline_prevails(self, mock_dt):
        scheduler = Scheduler()
        task1 = Task(start=datetime(2016, 1, 3),
                     end=datetime(2016, 3, 31))
        task2 = Task(start=datetime(2016, 1, 2),
                     end=datetime(2016, 4, 30))
        task3 = Task(start=datetime(2016, 1, 1),
                     end=datetime(2016, 5, 31))
        task4 = Task()
        mock_dt.now.return_value = datetime(2016, 2, 1)
        scheduled = scheduler.schedule([task3, task2, task1, task4])
        self.assertTrue(scheduled[0] is task1)
        self.assertTrue(scheduled[1] is task2)
        self.assertTrue(scheduled[2] is task3)
        self.assertTrue(scheduled[3] is task4)

    def test_task_with_earliest_creation_date_prevails_when_tasks_have_no_dates(self):
        scheduler = Scheduler()
        task1 = Task(creation=datetime(2016, 1, 3))
        task2 = Task(creation=datetime(2016, 1, 1))
        task3 = Task(creation=datetime(2016, 1, 15))
        task4 = Task(creation=datetime(2016, 1, 2))
        scheduled = scheduler.schedule([task1, task2, task3, task4])
        self.assertTrue(scheduled[0] is task2)
        self.assertTrue(scheduled[1] is task4)
        self.assertTrue(scheduled[2] is task1)
        self.assertTrue(scheduled[3] is task3)

    def test_task_with_earliest_creation_date_prevails_when_tasks_have_equal_deadlines(self):
        scheduler = Scheduler()
        task1 = Task(creation=datetime(2016, 1, 3),
                     end=datetime(2016, 5, 5))
        task2 = Task(creation=datetime(2016, 1, 1),
                     end=datetime(2016, 5, 5))
        scheduled = scheduler.schedule([task1, task2])
        self.assertTrue(scheduled[0] is task2)
        self.assertTrue(scheduled[1] is task1)

    @patch('task.datetime')
    def test_active_tasks_prevail_over_inactive_tasks(self, mock_dt):
        scheduler = Scheduler()
        active_task = Task(start=datetime(2016, 1, 1))
        inactive_task = Task(start=datetime(2016, 3, 3))
        mock_dt.now.return_value = datetime(2016, 2, 2)
        scheduled = scheduler.schedule([inactive_task, active_task])
        self.assertTrue(scheduled[0] is active_task)
        self.assertTrue(scheduled[1] is inactive_task)

    def test_tasks_with_higher_priority_prevail_over_tasks_with_lower_or_no_priority(self):
        scheduler = Scheduler()
        task1 = Task(priority=4)
        task2 = Task(priority=1)
        task3 = Task(priority=5)
        scheduled = scheduler.schedule([task1, task2, task3])
        self.assertTrue(scheduled[0] is task3)
        self.assertTrue(scheduled[1] is task1)
        self.assertTrue(scheduled[2] is task2)

    @patch('task.datetime')
    def test_active_tasks_with_daily_range_prevail_over_tasks_with_no_daily_range(self, mock_dt):
        scheduler = Scheduler()
        task_with_daily = Task(start=datetime(2016, 1, 1),
                               daily={'start': datetime(2016, 1, 1, 8, 0), 'end': datetime(2016, 1, 1, 16, 0)})
        task_no_daily = Task(start=datetime(2016, 1, 1))
        mock_dt.now.return_value = datetime(2016, 2, 2, 10, 0)
        scheduled = scheduler.schedule([task_no_daily, task_with_daily])
        self.assertTrue(scheduled[0] is task_with_daily)
        self.assertTrue(scheduled[1] is task_no_daily)


if __name__ == '__main__':
    unittest.main(verbosity=2)
