import unittest
from mock import Mock
from user import User
from user_repository_mongo import UserRepositoryMongo
from user_repository_test import UserRepositoryTest


class UserRepsitoryMongoTest(UserRepositoryTest):
    def setUp(self):
        super(UserRepsitoryMongoTest, self).setUp()
        self.mongo_collection = Mock()
        self.task_repository = UserRepositoryMongo(self.mongo_collection)


    def test_user_repository_should_assign_unique_id_after_adding_user(self):
        self.mongo_collection.submit_item.return_value = 10
        super(UserRepsitoryMongoTest, self).test_user_repository_should_assign_unique_id_after_adding_user()


    def test_user_repository_should_find_user_by_id_after_adding_user(self):
        self.mongo_collection.submit_item.return_value = 10
        self.mongo_collection.query_single.return_value = User(id=10)
        super(UserRepsitoryMongoTest, self).test_user_repository_should_find_user_by_id_after_adding_user()


if __name__ == '__main__':
    unittest.main()
