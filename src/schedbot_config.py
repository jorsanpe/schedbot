from user_repository_mongo import UserRepositoryMongo
from task_repository_mongo import TaskRepositoryMongo


def user_repo():
    return UserRepositoryMongo('localhost', '27017')


def task_repo():
    return TaskRepositoryMongo('localhost', '27017')

