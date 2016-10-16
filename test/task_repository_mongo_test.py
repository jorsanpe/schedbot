from mock import Mock, MagicMock
from task_repository_test import TaskRepositoryTest
from task_repository_mongo import TaskRepositoryMongo


class TaskRepositoryMongoTest(TaskRepositoryTest):
    def setUp(self):
        super(TaskRepositoryMongoTest, self).setUp()
        self.mongo_collection = Mock()
        self.task_repository = TaskRepositoryMongo(self.mongo_collection)


    def test_task_repository_should_assign_unique_id_after_adding_task(self):
        self.mongo_collection.submit_task.return_value = [self.a_task]

        super(TaskRepositoryMongoTest, self).test_task_repository_should_assign_unique_id_after_adding_task()


    def test_task_repository_should_return_task_list(self):
        self.mongo_collection.submit_task.return_value = [self.a_task]
        self.mongo_collection.query_multiple.return_value = [self.a_task]
        super(TaskRepositoryMongoTest, self).test_task_repository_should_return_task_list()


    def test_task_repository_should_maintain_different_task_lists_for_different_users(self):
        self.mongo_collection.submit_task = MagicMock(side_effect=[[self.a_task], [self.other_task]])
        self.mongo_collection.query_multiple = MagicMock(side_effect=[[self.a_task], [self.other_task], [self.a_task], [self.other_task]])
        super(TaskRepositoryMongoTest, self).test_task_repository_should_maintain_different_task_lists_for_different_users()
