import random
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x150")

number = random.randint(1, 100)

def check_guess():
    try:
        guess = int(entry.get())
        if guess == number:
            messagebox.showinfo("Result", "🎉 Correct! You guessed it.")
            root.quit()
        elif guess < number:
            messagebox.showinfo("Result", "Too low!")
        else:
            messagebox.showinfo("Result", "Too high!")
        entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

label = tk.Label(root, text="Enter your guess (1-100):")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Guess", command=check_guess)
button.pack(pady=10)

root.mainloop()