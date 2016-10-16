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


class MongoCollection:
    def __init__(self, host, port, collection_name):
        client = pymongo.MongoClient(self.host, self.port)
        self.collection = client.schedbot[collection_name]


    def query_single(self, *query):
        return self.collection.find_one(*query)


    def query_multiple(self, *query):
        return [Task(e) for e in self.collection.find(*query)]


    def submit_item(self, item):
        return self.collection.insert_one(item).inserted_id
