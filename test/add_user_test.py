import unittest
from mock import patch, MagicMock
from add_user import AddUser
from user_repository import UserRepository


class AddUserTest(unittest.TestCase):
    def setUp(self):
        self.user_repo = UserRepository()


    def test_add_user_should_add_user_to_repository(self):
        self.user_repo.user_exists = MagicMock(return_value=False)
        self.user_repo.add_user = MagicMock()
        add_user = AddUser(self.user_repo)

        response = add_user({'data': {'nickname': 'juancho'}})

        self.assertEqual('success', response['status'])


    def test_add_user_should_fail_if_user_already_exists(self):
        self.user_repo.user_exists = MagicMock(return_value=True)
        add_user = AddUser(self.user_repo)

        response = add_user({'data': {'nickname': 'juancho'}})

        self.assertEqual('fail', response['status'])
