@endpoint1/taskName/taskDate:
def storetask():
    1. go to database and in taskTable
    2. INSERT INTO taskTable VALUES (taskName, taskDate, status="incomplete")


@endpoint2
def getTasks():
    1. go to database in TaskTable
    2. SELECT taskName, taskDate FROM TaskTable
    3. put everything in a JSON object
    4. return JSON Object
