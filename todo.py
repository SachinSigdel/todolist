from tabulate import tabulate

class TodoList:
    task_id = 1
    def __init__(self,tasks,complete_status):
        self.task_id = TodoList.task_id
        self.tasks = tasks
        self.complete_status = complete_status
        TodoList.task_id+=1