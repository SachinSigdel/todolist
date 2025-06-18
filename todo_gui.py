import tkinter as tk
from tkinter import ttk,messagebox
from todo import TodoList

class TodoGUI:
    def __init__(self):
        self.todolist = []
        self.todo_task = {}
        self.root = tk.Tk()
        self.root.geometry("550x500")
        self.root.title("ToDo")
        self.display_frame = tk.Frame(self.root)
        self.display_frame.grid(row=3,column=0,columnspan=3)

        self.task_entry = tk.Entry(self.root,width=40)
        self.task_entry.grid(row=0,column=0,columnspan=2,pady=10)

        add_btn = tk.Button(self.root,text="Add Task", command=self.add_and_display)
        add_btn.grid(row=0,column=2,pady=10)

        title = tk.Label(self.root, text="Your Tasks:")
        title.grid(row=1,column=0,columnspan=3,pady=10)

        self.root.mainloop()

    def add_and_display(self):
        self.add_task()
        self.display()

    def add_task(self):
        user_task = self.task_entry.get()
        if user_task.strip():
            newTask = TodoList(user_task,"✖ Incomplete")
            self.todo_task = {
                "Id": str(newTask.task_id),
                "Task":newTask.tasks,
                "Complete Status": str(newTask.complete_status)
            }
            self.todolist.append(self.todo_task)
            messagebox.showinfo("Added","New Task Added")
        else:
            messagebox.showwarning("Empty task", "Please enter a task!")

    def display(self):
    # Clear the frame first
        for widget in self.display_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.todolist):
            tk.Label(self.display_frame, text="ID").grid(row=0,column=0,padx=10,pady=10)
            tk.Label(self.display_frame, text="Task").grid(row=0,column=1,padx=10,pady=10)
            tk.Label(self.display_frame, text="Status").grid(row=0,column=2,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Id"]).grid(row=index+1, column=0,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Task"]).grid(row=index+1, column=1,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Complete Status"]).grid(row=index+1, column=2,padx=10,pady=10)

            tk.Button(self.display_frame, text="Complete", 
                    command=lambda task_id=task["Id"]: self.complete_task(task_id)
                    ).grid(row=index+1, column=3,padx=10,pady=10)
            tk.Button(self.display_frame, text="Delete", 
                    command=lambda task_id=task["Id"]: self.delete_task(task_id)
                    ).grid(row=index+1,column=4,padx=10,pady=10)

    def complete_task(self,task_id):
        for each in self.todolist:
            if str(task_id) == each["Id"]:
                each["Complete Status"] = "✔ Complete"
                messagebox.showinfo("Completed","Task completed!")
                self.display()
                return

    def delete_task(self,id):
        for each in self.todolist:
            if str(id) == each["Id"]:
                self.todolist.remove(each)
                messagebox.showinfo("Deleted","Task deleted succesfully!")
                self.display()
                return

TodoGUI()