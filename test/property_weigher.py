from elo import rate_1vs1

task_schema = {
    'creation': 1000,
    'start-date': 1000,
    'end-date': 1000,
    'duration': 1000,
    'priority': 1000,
    'daily-range': 1000,
}


for k1,v1 in task_schema.iteritems():
    for k2,v2 in task_schema.iteritems():
        (task_schema[k1], task_schema[k2]) = rate_1vs1()

