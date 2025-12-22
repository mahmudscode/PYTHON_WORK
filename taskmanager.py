import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.root.geometry("500x400")
        self.tasks = []

        # Title Label
        title = tk.Label(root, text="Task Manager", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Frame for input
        input_frame = tk.Frame(root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Task:").pack(side=tk.LEFT, padx=5)
        self.task_entry = tk.Entry(input_frame, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=5)

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Task", command=self.add_task, bg="green", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Delete Task", command=self.delete_task, bg="red", fg="white").pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Mark Done", command=self.mark_done, bg="blue", fg="white").pack(side=tk.LEFT, padx=5)

        # Listbox for tasks
        tk.Label(root, text="Tasks:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20)
        self.task_listbox = tk.Listbox(root, height=12, width=60)
        self.task_listbox.pack(padx=20, pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append({"task": task, "done": False, "time": datetime.now().strftime("%Y-%m-%d %H:%M")})
            self.task_entry.delete(0, tk.END)
            self.refresh_listbox()
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks.pop(index)
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_done(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.tasks[index]["done"] = True
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to mark done!")

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task_dict in enumerate(self.tasks):
            status = "✓" if task_dict["done"] else "○"
            display = f"{status} {task_dict['task']} ({task_dict['time']})"
            self.task_listbox.insert(tk.END, display)

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()