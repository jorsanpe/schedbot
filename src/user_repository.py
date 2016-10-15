# -*- coding: utf-8 -*-
# Copyright 2016 Jordi Sánchez
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

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
