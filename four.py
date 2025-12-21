import random
import tkinter as tk
from tkinter import messagebox


def roll_dice():
    try:
        num_dice = int(dice_entry.get())
        sides = int(sides_entry.get())

        if num_dice < 1 or sides < 1:
            raise ValueError

        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        result_label.config(
            text=f"Rolled: {rolls}\nTotal: {sum(rolls)}"
        )

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter positive numbers.")


# GUI Window
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("350x300")
root.resizable(False, False)

# Title
tk.Label(root, text="🎲 Dice Rolling Simulator", font=("Arial", 16, "bold")).pack(pady=10)

# Dice Input
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Number of Dice:").grid(row=0, column=0, padx=5, pady=5)
dice_entry = tk.Entry(frame, width=10)
dice_entry.grid(row=0, column=1)

tk.Label(frame, text="Sides per Die:").grid(row=1, column=0, padx=5, pady=5)
sides_entry = tk.Entry(frame, width=10)
sides_entry.grid(row=1, column=1)

# Roll Button
tk.Button(root, text="Roll Dice 🎲", font=("Arial", 12), command=roll_dice).pack(pady=15)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
