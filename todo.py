from tabulate import tabulate

todo_list = []
task_id = 1
def add_new_task():
    tasks = []
    task = input("\nEnter your task for the day: ")
    complete_status = False
    tasks.append(task_id)
    tasks.append(task)
    tasks.append(complete_status)
    return tasks

def display():
    headers = ["Id","Tasks","Complete Status"]
    print(tabulate(todo_list, headers=headers, tablefmt="grid"))

def complete_task(id):
    for each in todo_list:
        if each[0] == id:
            each[2] = True
            return
    print("Task not found!")

add_more = True
while add_more == True:
    print("\n")
    add_new = input("Add new task? (y/n)")
    if add_new.lower() == "y":
        todo_list.append(add_new_task())
        task_id += 1
        print("\n")
        display()
    elif add_new.lower() == "n":
        add_more = False
    else:
        print("\nChoose a valid option!")

loop2 = True
while loop2 == True:
    complete = input("Is a task completed? (y/n)")
    if complete.lower() == "y":
        try:
            print("\n")
            complete_id = int(input("Enter the id of the task which is completed: "))
            complete_task(complete_id)
            print("\n")
            display()
        except ValueError:
            print("Invalid ID!")
    elif complete.lower() == "n":
        loop2 = False
    else:
        print("Enter a valid option!")