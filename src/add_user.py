import response
from user import User


class AddUser:
    def __init__(self, user_repo):
        self.user_repo = user_repo


    def __call__(self, request):
        new_user = User(**request['data'])
        if self.user_repo.user_exists(new_user):
            return response.user_already_exists()
        self.user_repo.add_user(new_user)
        return response.user_created()
