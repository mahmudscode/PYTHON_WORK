import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("1920x1080")
        self.current_player = "X"
        self.board = ["" for _ in range(9)]
        self.buttons = []
        self.dark_mode = False
        
        self.label = tk.Label(root, text="Player X's Turn", font=("Arial", 14))
        self.label.pack(pady=10)
        
        frame = tk.Frame(root)
        frame.pack()
        
        for i in range(9):
            btn = tk.Button(frame, text="", font=("Arial", 20), width=20, height=8,
                          command=lambda idx=i: self.click(idx))
            btn.grid(row=i//3, column=i%3, padx=5, pady=5)
            self.buttons.append(btn)
        
        reset_btn = tk.Button(root, text="Reset Game", font=("Arial", 12), command=self.reset)
        reset_btn.pack(pady=10)
        
        theme_btn = tk.Button(root, text="Toggle Theme", font=("Arial", 10), command=self.toggle_theme)
        theme_btn.pack(pady=5)
        
        self.apply_theme()
    
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
    
    def apply_theme(self):
        if self.dark_mode:
            bg_color = "#2b2b2b"
            fg_color = "white"
            btn_color = "#404040"
        else:
            bg_color = "white"
            fg_color = "black"
            btn_color = "#f0f0f0"
        
        self.root.config(bg=bg_color)
        self.label.config(bg=bg_color, fg=fg_color)
        
        for btn in self.buttons:
            btn.config(bg=btn_color, fg=fg_color)
    
    def click(self, idx):
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.label.config(text=f"Player {self.current_player}'s Turn")
    
    def check_winner(self):
        winning_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combos:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False
    
    def reset(self):
        self.board = ["" for _ in range(9)]
        self.current_player = "X"
        self.label.config(text="Player X's Turn")
        for btn in self.buttons:
            btn.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()