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

from task_repository import TaskRepository


class TaskRepositoryMongo(TaskRepository):
    def __init__(self, mongo_client):
        self.client = mongo_client  # pymongo.MongoClient(self.host, self.port)


    def tasks_for(self, user):
        return self.client.query_multiple({'user_id': user['id']})


    def add_task_for(self, user, new_task):
        new_task['user_id'] = user['id']
        task_id = self.client.submit_task(new_task.as_dict())
        new_task['id'] = str(task_id)
        return self.tasks_for(user)


    def update_tasks_for(self, user, scheduled_task_list):
        pass
