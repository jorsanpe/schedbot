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

        new_task = Task(**request['data'])
        self.task_repo.add_task_for(user, new_task)
        task_list = self.task_repo.tasks_for(user)
        scheduled_task_list = scheduler.schedule(task_list)
        self.task_repo.update_tasks_for(user, scheduled_task_list)

        return response.json_with(scheduled_task_list)
