from tabulate import tabulate

todo_list = []
def add_new_task():
    tasks = []
    task = input("\nEnter your task for the day: ")
    complete_status = False
    task_id = 1
    tasks.append(task_id)
    tasks.append(task)
    tasks.append(complete_status)
    task_id += 1
    return tasks

todo_list.append(add_new_task())

headers = ["Id","Tasks","Compete Status"]
print(tabulate(todo_list, headers=headers, tablefmt="grid"))