def keys_match(d, **kwargs):
    for k, v in kwargs.iteritems():
        if d[k] != v:
            return False
    return True


class UserRepository:
    def __init__(self):
        self.user_list = []


    def find_one(self, **kwargs):
        return next(u for u in self.user_list if keys_match(u, **kwargs))


    def add_user(self, user):
        self.user_list.append(user)
        user['id'] = len(self.user_list)


    def user_exists(self, user):
        any(u for u in self.user_list if keys_match(u, nickname=user['nickname'], email=user['email']))
