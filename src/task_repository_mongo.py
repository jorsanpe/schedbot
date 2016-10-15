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
