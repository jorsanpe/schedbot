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
