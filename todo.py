from tabulate import tabulate

class TodoList:
    # class to create object of every task and pass it to dictionary later
    task_id = 1 #id given to particular task
    def __init__(self,tasks,complete_status):
        self.task_id = TodoList.task_id
        self.tasks = tasks
        self.complete_status = complete_status
        TodoList.task_id+=1