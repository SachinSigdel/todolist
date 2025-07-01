import tkinter as tk
from tkinter import ttk,messagebox
from todo import TodoList

class TodoGUI:
    def __init__(self):
        # declaring list and dictionary to store tasks
        self.todolist = []
        self.todo_task = {}
        # creating the frame for gui
        self.root = tk.Tk()
        self.root.geometry("550x500")
        self.root.title("ToDo")
        # frame to display tasks
        self.display_frame = tk.Frame(self.root)
        self.display_frame.grid(row=3,column=0,columnspan=3)
        #text box for user to enter their tasks 
        self.task_entry = tk.Entry(self.root,width=40)
        self.task_entry.grid(row=0,column=0,columnspan=2,pady=10)
        # button to add the task 
        add_btn = tk.Button(self.root,text="Add Task", command=self.add_and_display)
        add_btn.grid(row=0,column=2,pady=10)
        # title for display
        title = tk.Label(self.root, text="Your Tasks:")
        title.grid(row=1,column=0,columnspan=3,pady=10)
        # running the gui
        self.root.mainloop()

    def add_and_display(self):
        """
        function to add task and display at the same time
        """
        self.add_task()
        self.display()

    def add_task(self):
        """
        function to add task to the dictionary
        """
        # getting the task from user
        user_task = self.task_entry.get()
        if user_task.strip():
            newTask = TodoList(user_task,"✖ Incomplete")
            self.todo_task = {
                "Id": str(newTask.task_id),
                "Task":newTask.tasks,
                "Complete Status": str(newTask.complete_status)
            }
            # add the task_dict to task_list
            self.todolist.append(self.todo_task)
            messagebox.showinfo("Added","New Task Added")
        else:
            messagebox.showwarning("Empty task", "Please enter a task!")

    def display(self):
        # Clear the frame first
        for widget in self.display_frame.winfo_children():
            widget.destroy()
        # get every task from tasklist and display it using tk.grid in a loop.
        for index, task in enumerate(self.todolist):
            # capture the id of the current task to run complete and delete tasks.
            task_id=task["Id"]
            tk.Label(self.display_frame, text="ID").grid(row=0,column=0,padx=10,pady=10)
            tk.Label(self.display_frame, text="Task").grid(row=0,column=1,padx=10,pady=10)
            tk.Label(self.display_frame, text="Status").grid(row=0,column=2,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Id"]).grid(row=index+1, column=0,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Task"]).grid(row=index+1, column=1,padx=10,pady=10)
            tk.Label(self.display_frame, text=task["Complete Status"]).grid(row=index+1, column=2,padx=10,pady=10)
            # button to run complete task function
            tk.Button(self.display_frame, text="Complete", command=lambda: self.complete_task(task_id)).grid(row=index+1, column=3,padx=10,pady=10)
            # button to run delete task function
            tk.Button(self.display_frame, text="Delete", command=lambda: self.delete_task(task_id)).grid(row=index+1,column=4,padx=10,pady=10)

    def complete_task(self,id):
        """
        function to complete task using it's id.
        """
        for each in self.todolist:
            # get captured id from the loop and pass it to the conditional statement
            if str(id) == each["Id"]:
                each["Complete Status"] = "✔ Complete"
                messagebox.showinfo("Completed","Task completed!")
                self.display()
                return

    def delete_task(self,id):
        """
        function to delete task using it's id.
        """
        for each in self.todolist:
            # get captured id from the loop and pass it to the conditional statement
            if str(id) == each["Id"]:
                self.todolist.remove(each)
                messagebox.showinfo("Deleted","Task deleted succesfully!")
                self.display()
                return

TodoGUI()