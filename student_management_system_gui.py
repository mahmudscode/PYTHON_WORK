import tkinter as tk
from tkinter import messagebox

FILE_NAME = "students.txt"

# ---------------- File Handling ----------------
def load_students():
    students = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                sid, name, dept, cgpa = line.strip().split(",")
                students.append([sid, name, dept, cgpa])
    except FileNotFoundError:
        pass
    return students


def save_students(students):
    with open(FILE_NAME, "w") as file:
        for s in students:
            file.write(",".join(s) + "\n")


# ---------------- Core Functions ----------------
def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    cgpa = entry_cgpa.get()

    if not sid or not name or not dept or not cgpa:
        messagebox.showerror("Error", "All fields are required!")
        return

    students.append([sid, name, dept, cgpa])
    save_students(students)
    clear_entries()
    view_students()
    messagebox.showinfo("Success", "Student Added Successfully!")


def view_students():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(tk.END, f"ID:{s[0]} | Name:{s[1]} | Dept:{s[2]} | CGPA:{s[3]}")


def search_student():
    sid = entry_id.get()
    for s in students:
        if s[0] == sid:
            entry_name.delete(0, tk.END)
            entry_dept.delete(0, tk.END)
            entry_cgpa.delete(0, tk.END)

            entry_name.insert(0, s[1])
            entry_dept.insert(0, s[2])
            entry_cgpa.insert(0, s[3])
            return
    messagebox.showerror("Error", "Student Not Found!")


def update_student():
    sid = entry_id.get()
    for s in students:
        if s[0] == sid:
            s[1] = entry_name.get()
            s[2] = entry_dept.get()
            s[3] = entry_cgpa.get()
            save_students(students)
            view_students()
            messagebox.showinfo("Success", "Student Updated Successfully!")
            return
    messagebox.showerror("Error", "Student Not Found!")


def delete_student():
    sid = entry_id.get()
    for s in students:
        if s[0] == sid:
            students.remove(s)
            save_students(students)
            clear_entries()
            view_students()
            messagebox.showinfo("Success", "Student Deleted!")
            return
    messagebox.showerror("Error", "Student Not Found!")


def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_cgpa.delete(0, tk.END)


# ---------------- GUI Design ----------------
students = load_students()

root = tk.Tk()
root.title("Student Management System")
root.geometry("650x500")
root.resizable(False, False)

title = tk.Label(root, text="Student Management System", font=("Arial", 18, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Student ID").grid(row=0, column=0, padx=5, pady=5)
tk.Label(frame, text="Name").grid(row=1, column=0, padx=5, pady=5)
tk.Label(frame, text="Department").grid(row=2, column=0, padx=5, pady=5)
tk.Label(frame, text="CGPA").grid(row=3, column=0, padx=5, pady=5)

entry_id = tk.Entry(frame)
entry_name = tk.Entry(frame)
entry_dept = tk.Entry(frame)
entry_cgpa = tk.Entry(frame)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_dept.grid(row=2, column=1)
entry_cgpa.grid(row=3, column=1)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="View", width=12, command=view_students).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Search", width=12, command=search_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Update", width=12, command=update_student).grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="Delete", width=12, command=delete_student).grid(row=0, column=4, padx=5)

listbox = tk.Listbox(root, width=90, height=10)
listbox.pack(pady=10)

view_students()
root.mainloop()
