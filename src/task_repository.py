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

class TaskRepository:
    def __init__(self):
        self.next_id = 0
        self.task_list = {}


    def tasks_for(self, user):
        return self.task_list[user['id']]


    def add_task_for(self, user, new_task):
        if not self.task_list.has_key(user['id']):
            self.task_list[user['id']] = []

        new_task['id'] = self.next_id
        self.next_id += 1
        self.task_list[user['id']].append(new_task)


    def update_tasks_for(self, user, scheduled_task_list):
        pass
