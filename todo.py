from tabulate import tabulate

tasks = {}
task_id = 1
add_new_task = True
while add_new_task == True:
    task = input("Enter your task for the day: ")
    tasks[task_id] = task
    task_id += 1
    more_task = input("\nDo you want to add more tasks?(y/n)")
    if more_task.strip().lower() == "y":
        add_new_task == True
    elif more_task.strip().lower() == "n":
        add_new_task == False
        break
    else:
        print("Choose a valid option!")

headers = ["Id","Tasks"]

print(tabulate(tasks.items(), headers=headers, tablefmt="grid"))