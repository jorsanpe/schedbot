import unittest
from user_repository import UserRepository
from user import User


class UserRepositoryTest(unittest.TestCase):
    def test_user_repository_should_assign_unique_id_after_adding_user(self):
        user_repository = UserRepository()
        user = User()

        user_repository.add_user(user)

        self.assertTrue(user['id'] >= 0)


    def test_user_repository_should_find_user_by_id_after_adding_user(self):
        user_repository = UserRepository()
        user = User()

        user_repository.add_user(user)

        self.assertEqual(user, user_repository.find_one(id=user['id']))
