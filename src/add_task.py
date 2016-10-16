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

import scheduler
from task import Task
import response


class AddTask:
    def __init__(self, user_repo, task_repo):
        self.user_repo = user_repo
        self.task_repo = task_repo


    def __call__(self, request):
        user = self.user_repo.find_one(request['user'])
        if not user:
            return response.user_not_found()

        self.add_task_to_repository(request, user)
        scheduled_task_list = self.schedule_user_task_list(user)
        return response.dict_with(scheduled_task_list)


    def schedule_user_task_list(self, user):
        task_list = self.task_repo.tasks_for(user)
        scheduled_task_list = scheduler.schedule(task_list)
        self.task_repo.update_tasks_for(user, scheduled_task_list)
        return scheduled_task_list


    def add_task_to_repository(self, request, user):
        new_task = Task(**request['data'])
        self.task_repo.add_task_for(user, new_task)
