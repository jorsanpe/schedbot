user_schema = {
    'id': 'integer',
    'email': 'string',
    'nickname': 'string',
}

task_schema = {
    'title': 'string',
    'description': 'string',
    'creation': 'date',
    'start': 'date',
    'end': 'date',
    'duration': 'date',
    'priority': 'integer',
    'timezone': 'string',
    'daily': {
        'start': 'hour',
        'end': 'hour',
    },
    'after': 'task-list',
    'before': 'task-list',
    'parent': 'task',
    'schedule': '',
    'finished': '',
}

request_schema = {
    'user': 'string',
    'code': 'string',
}

response_schema = {
    'status': ['fail','success'],
}