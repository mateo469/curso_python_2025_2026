import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Gato 🐱 | Tic Tac Toe")
        self.root.resizable(False, False)
        self.turn = "X"
        self.board = [""] * 9
        self.buttons = []
        self.dark_bg = "#121212"
        self.button_bg = "#1E1E1E"
        self.text_color = "white"
        self.accent_color = "#4CAF50"
        self.root.configure(bg=self.dark_bg)
        self.create_widgets()

    def create_widgets(self):
        title = tk.Label(self.root, text="Juego de Gato 🐾", font=("Arial", 24, "bold"),
                         bg=self.dark_bg, fg=self.text_color)
        title.grid(row=0, column=0, columnspan=3, pady=(10, 20))

        for i in range(9):
            button = tk.Button(
                self.root,
                text="",
                font=("Arial", 32),
                width=5,
                height=2,
                bg=self.button_bg,
                fg=self.text_color,
                activebackground="#333333",
                activeforeground=self.text_color,
                command=lambda i=i: self.button_click(i)
            )
            button.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)

        reset_btn = tk.Button(
            self.root,
            text="Reiniciar 🔄",
            font=("Arial", 14),
            bg=self.accent_color,
            fg="white",
            activebackground="#45A049",
            command=self.reset_game
        )
        reset_btn.grid(row=4, column=0, columnspan=3, pady=(10, 10))

    def button_click(self, index):
        if self.buttons[index]["text"] == "" and self.check_winner() is None:
            self.buttons[index]["text"] = self.turn
            self.board[index] = self.turn
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            else:
                self.turn = "O" if self.turn == "X" else "X"

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)
        ]
        for a, b, c in combos:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "":
                return self.board[a]
        if "" not in self.board:
            return "Empate"
        return None

    def end_game(self, winner):
        if winner == "Empate":
            messagebox.showinfo("Empate", "¡Es un empate!")
        else:
            messagebox.showinfo("Ganador", f"¡El jugador {winner} ha ganado!")
        self.disable_buttons()

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state=tk.DISABLED)

    def reset_game(self):
        self.turn = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state=tk.NORMAL)

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
