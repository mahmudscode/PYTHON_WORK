import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.tasks_file = "tasks.json"
        self.tasks = self.load_tasks()
        
        # Title
        title = tk.Label(root, text="My To-Do List", font=("Arial", 18, "bold"))
        title.pack(pady=10)
        
        # Listbox
        self.listbox = tk.Listbox(root, height=15, width=50)
        self.listbox.pack(pady=10, padx=10)
        self.refresh_listbox()
        
        # Button frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)
        
        # Add button
        add_btn = tk.Button(button_frame, text="Add Task", command=self.add_task, bg="green", fg="white")
        add_btn.grid(row=0, column=0, padx=5)
        
        # Delete button
        delete_btn = tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="red", fg="white")
        delete_btn.grid(row=0, column=1, padx=5)
        
        # Complete button
        complete_btn = tk.Button(button_frame, text="Mark Complete", command=self.complete_task, bg="blue", fg="white")
        complete_btn.grid(row=0, column=2, padx=5)
    
    def load_tasks(self):
        if os.path.exists(self.tasks_file):
            with open(self.tasks_file, "r") as f:
                return json.load(f)
        return []
    
    def save_tasks(self):
        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f)
    
    def refresh_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            self.listbox.insert(tk.END, f"{status} {task['name']}")
    
    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            self.tasks.append({"name": task_name, "completed": False})
            self.save_tasks()
            self.refresh_listbox()
    
    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks.pop(index)
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete")
    
    def complete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()