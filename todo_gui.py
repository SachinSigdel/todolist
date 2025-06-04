import tkinter as tk
from tkinter import ttk,messagebox
from todo import TodoList

class TodoGUI:
    def __init__(self):
        self.todolist = []
        self.todo_task = {}
        self.root = tk.Tk()
        self.root.geometry("620x600")
        self.root.title("ToDo")

        self.task_entry = tk.Entry(self.root,width=40)
        self.task_entry.place(x=10,y=10,width=500)

        add_btn = tk.Button(self.root,text="Add Task", command=self.add_task)
        add_btn.place(x=520,y=10)

        display_btn = tk.Button(self.root,text="Display your tasks", command=self.display)
        display_btn.place(x=250,y=50)

        columns = ["Id","Tasks","Complete Status"]
        self.tree = ttk.Treeview(self.root, columns=columns, show="headings")
        self.tree.place(x=10,y=90)
        for col in columns:
            self.tree.heading(col, text=col)

        id_label = tk.Label(self.root, text="Enter Id:")
        id_label.place(x=10,y=310)

        self.id_entry = tk.Entry(self.root)
        self.id_entry.place(x=70,y=310,width=300)

        complete_btn = tk.Button(self.root,text="complete task",command=self.complete_task)
        complete_btn.place(x=380,y=310)

        delete_btn = tk.Button(self.root,text="delete task",command=self.delete_task)
        delete_btn.place(x=500,y=310)

        self.root.mainloop()

    def add_task(self):
        user_task = self.task_entry.get()
        if user_task.strip():
            newTask = TodoList(user_task,"❌")
            self.todo_task = {
                "Id": str(newTask.task_id),
                "Task":newTask.tasks,
                "Complete Status": str(newTask.complete_status)
            }
            self.todolist.append(self.todo_task)
            messagebox.showinfo("Added","New Task Added")

    def display(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for each in self.todolist:
            row = [each["Id"], each["Task"], each["Complete Status"]]
            self.tree.insert("", tk.END, values=row)

    def complete_task(self):
        id = self.id_entry.get()
        if id.strip():
            for each in self.todolist:
                if str(id) == each["Id"]:
                    each["Complete Status"] = "✔ Done"
                    messagebox.showinfo("Deleted","Task completed!")
                    self.display()
                    return
        else:
            messagebox.showerror("Error","Please provide an Id")

    def delete_task(self):
        id = self.id_entry.get()
        if id.strip():
            for each in self.todolist:
                if str(id) == each["Id"]:
                    self.todolist.remove(each)
                    messagebox.showinfo("Deleted","Task deleted succesfully!")
                    self.display()
                    return
        else:
            messagebox.showerror("Error","Please provide an Id")

TodoGUI()