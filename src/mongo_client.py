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

import pymongo
from task import Task


class MongoClient:
    def __init__(self, host, port):
        self.client = pymongo.MongoClient(self.host, self.port)


    def query_single(self, *query):
        tasks = self.client.schedbot.tasks
        return tasks.find_one(*query)


    def query_multiple(self, *query):
        tasks = self.client.schedbot.tasks
        return [Task(e) for e in tasks.find(*query)]


    def submit_task(self, task):
        return self.client.schedbot.tasks.insert_one(task).inserted_id
