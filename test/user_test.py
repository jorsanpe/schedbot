import unittest
from user import User


class TaskTest(unittest.TestCase):
    def test_user_should_provide_accessors_to_its_propierties(self):
        user = User(name='juancho')

        self.assertEqual('juancho', user['name'])
