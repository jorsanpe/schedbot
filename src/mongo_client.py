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
