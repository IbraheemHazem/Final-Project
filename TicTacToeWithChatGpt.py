# import tkinter as tk
# import random

# class TicTacToe:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tic Tac Toe")

#         self.player = "X"
#         self.computer = "O"

#         self.buttons = [[None, None, None] for _ in range(3)]

#         self.score_player = 0
#         self.score_computer = 0
#         self.score_draw = 0

#         self.message_label = tk.Label(root, text="", font=("Helvetica", 16))
#         self.message_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

#         for i in range(3):
#             for j in range(3):
#                 self.buttons[i][j] = tk.Button(root, text="", font=("Helvetica", 16), width=6, height=3,
#                                                command=lambda i=i, j=j: self.click_button(i, j))
#                 self.buttons[i][j].grid(row=i + 1, column=j, padx=5, pady=5)

#         self.score_label_player = tk.Label(root, text="Player: 0", font=("Helvetica", 14))
#         self.score_label_player.grid(row=4, column=0, padx=5, pady=5)

#         self.score_label_computer = tk.Label(root, text="Computer: 0", font=("Helvetica", 14))
#         self.score_label_computer.grid(row=4, column=1, padx=5, pady=5)

#         self.score_label_draw = tk.Label(root, text="Draw: 0", font=("Helvetica", 14))
#         self.score_label_draw.grid(row=4, column=2, padx=5, pady=5)

#         self.reset_board()

#     def reset_board(self):
#         for i in range(3):
#             for j in range(3):
#                 self.buttons[i][j].config(text="", state=tk.NORMAL)

#         self.message_label.config(text="")

#     def click_button(self, i, j):
#         if self.buttons[i][j]["text"] == "":
#             self.buttons[i][j]["text"] = self.player
#             self.buttons[i][j]["state"] = tk.DISABLED

#             if self.check_winner(self.player):
#                 self.message_label.config(text="Player wins!", fg="green")
#                 self.score_player += 1
#                 self.update_scores()
#                 self.reset_board()
#             elif self.check_draw():
#                 self.message_label.config(text="It's a draw!", fg="orange")
#                 self.score_draw += 1
#                 self.update_scores()
#                 self.reset_board()
#             else:
#                 self.computer_move()

#     def computer_move(self):
#         available_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]
#         if available_cells:
#             i, j = random.choice(available_cells)
#             self.buttons[i][j]["text"] = self.computer
#             self.buttons[i][j]["state"] = tk.DISABLED

#             if self.check_winner(self.computer):
#                 self.message_label.config(text="Computer wins!", fg="red")
#                 self.score_computer += 1
#                 self.update_scores()
#                 self.reset_board()
#             elif self.check_draw():
#                 self.message_label.config(text="It's a draw!", fg="orange")
#                 self.score_draw += 1
#                 self.update_scores()
#                 self.reset_board()

#     def check_winner(self, symbol):
#         # Check rows
#         for i in range(3):
#             if all(self.buttons[i][j]["text"] == symbol for j in range(3)):
#                 return True

#         # Check columns
#         for j in range(3):
#             if all(self.buttons[i][j]["text"] == symbol for i in range(3)):
#                 return True

#         # Check diagonals
#         if all(self.buttons[i][i]["text"] == symbol for i in range(3)) or \
#                 all(self.buttons[i][2 - i]["text"] == symbol for i in range(3)):
#             return True

#         return False

#     def check_draw(self):
#         return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

#     def update_scores(self):
#         self.score_label_player.config(text=f"Player: {self.score_player}")
#         self.score_label_computer.config(text=f"Computer: {self.score_computer}")
#         self.score_label_draw.config(text=f"Draw: {self.score_draw}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TicTacToe(root)
#     root.mainloop()



# import tkinter as tk
# from tkinter import messagebox
# import random

# class TicTacToe:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tic-Tac-Toe Game")
#         self.root.configure(bg='#D7BDE2')
#         self.root.iconbitmap("TicTacToe.ico")

#         self.pc_wins = 0
#         self.player_wins = 0

#         self.buttons = [[None, None, None] for _ in range(3)]

#         self.players = ["X", "O"]
#         self.current_player = random.choice(self.players)
#         self.current_player = self.players[0]

#         self.create_gui()

#     def create_gui(self):
#         self.create_score_labels()
#         self.create_turn_label()
#         self.create_restart_button()
#         self.create_game_board()

#     def create_score_labels(self):
#         self.player_score_label = tk.Label(self.root, text=f"You: {self.player_wins}", font=("Arial", 20), bg="#3498DB")
#         self.player_score_label.pack(anchor="center")

#         self.pc_score_label = tk.Label(self.root, text=f"Computer: {self.pc_wins}", font=("Arial", 20), bg="cyan")
#         self.pc_score_label.pack(anchor="center")

#     def create_turn_label(self):
#         self.turn_label = tk.Label(self.root, text=f"{self.current_player}'s Turn", font=("Arial", 40), bg="#D7BDE2")
#         self.turn_label.pack(side="top")

#     def create_restart_button(self):
#         self.restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 15), padx=45, pady=15,
#                                      command=self.new_game, borderwidth=3, bg="#8E44AD", fg="#000000")
#         self.restart_btn.pack(side="top")

#     def create_game_board(self):
#         frame = tk.Frame(self.root)
#         frame.pack()

#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col] = tk.Button(frame, text="", font=("Arial", 40), width=6, height=2,
#                                                    command=lambda row=row, col=col: self.next_turn(row, col), bg="#8E44AD")
#                 self.buttons[row][col].grid(row=row, column=col)

#     def new_game(self):
#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col]["text"] = ""
#                 self.buttons[row][col].config(bg="#8E44AD")

#         self.turn_label["text"] = f"{self.current_player}'s Turn"
#         self.current_player = self.players[0]

#     def next_turn(self, row, col):
#         if self.buttons[row][col]['text'] == "" and not self.winner():
#             self.buttons[row][col]['text'] = self.current_player

#             if not self.winner():
#                 self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
#                 self.turn_label.config(text=f"{self.current_player}'s Turn")
#                 self.computer_move()

#             elif self.winner() == "player":
#                 self.turn_label.config(text=f"{self.players[0]} Wins")
#                 self.player_wins += 1
#                 self.update_scores()
#                 messagebox.showinfo("Game Over", "You win!")

#             elif self.winner() == "computer":
#                 self.turn_label.config(text=f"{self.players[1]} Wins")
#                 self.pc_wins += 1
#                 self.update_scores()
#                 messagebox.showinfo("Game Over", "You Lose!")

#             elif self.winner() == "tie":
#                 self.turn_label.config(text="Tie round, No Winner!")
#                 messagebox.showinfo("Game Over", "It's a tie!")

#     def computer_move(self):
#         if self.current_player == self.players[1]:
#             row, col = self.get_computer_move()
#             self.next_turn(row, col)

#     def get_computer_move(self):
#         empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
#         return random.choice(empty_cells)

#     def winner(self):
#         for i in range(3):
#             if (self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != ""):
#                 self.highlight_winner_cells(i, 0, i, 1, i, 2)
#                 return "player" if self.buttons[i][0]['text'] == self.players[0] else "computer"

#             if (self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ""):
#                 self.highlight_winner_cells(0, i, 1, i, 2, i)
#                 return "player" if self.buttons[0][i]['text'] == self.players[0] else "computer"

#         if (self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != ""):
#             self.highlight_winner_cells(0, 0, 1, 1, 2, 2)
#             return "player" if self.buttons[0][0]['text'] == self.players[0] else "computer"

#         if (self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ""):
#             self.highlight_winner_cells(0, 2, 1, 1, 2, 0)
#             return "player" if self.buttons[0][2]['text'] == self.players[0] else "computer"

#         if not any(self.buttons[i][j]['text'] == "" for i in range(3) for j in range(3)):
#             self.highlight_tie_cells()
#             return "tie"

#         return False

#     def highlight_winner_cells(self, x1, y1, x2, y2, x3, y3):
#         self.buttons[x1][y1].config(bg="#3498DB")
#         self.buttons[x2][y2].config(bg="#3498DB")
#         self.buttons[x3][y3].config(bg="#3498DB")

#     def highlight_tie_cells(self):
#         for i in range(3):
#             for j in range(3):
#                 self.buttons[i][j].config(bg="red")

#     def update_scores(self):
#         self.player_score_label.config(text=f"You: {self.player_wins}")
#         self.pc_score_label.config(text=f"Computer: {self.pc_wins}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TicTacToe(root)
#     root.mainloop()





# import tkinter as tk
# from tkinter import messagebox
# import random

# class TicTacToe:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Tic-Tac-Toe Game")
#         self.root.configure(bg='#ecf0f1')
#         # self.root.iconbitmap("unnamed.ico")

#         self.pc_wins = 0
#         self.player_wins = 0

#         self.buttons = [[None, None, None] for _ in range(3)]

#         self.players = ["X", "O"]
#         self.current_player = random.choice(self.players)

#         self.create_gui()

#     def create_gui(self):
#         self.create_score_labels()
#         self.create_turn_label()
#         self.create_restart_button()
#         self.create_game_board()

#     def create_score_labels(self):
#         self.player_score_label = tk.Label(self.root, text=f"You: {self.player_wins}", font=("Arial", 20), bg="#3498DB", fg="white")
#         self.player_score_label.pack(anchor="center")

#         self.pc_score_label = tk.Label(self.root, text=f"Computer: {self.pc_wins}", font=("Arial", 20), bg="cyan", fg="white")
#         self.pc_score_label.pack(anchor="center")

#     def create_turn_label(self):
#         self.turn_label = tk.Label(self.root, text=f"{self.current_player}'s Turn", font=("Arial", 40), bg='#ecf0f1')
#         self.turn_label.pack(side="top")

#     def create_restart_button(self):
#         self.restart_btn = tk.Button(self.root, text="Restart", font=("Arial", 15), padx=45, pady=15,
#                                      command=self.new_game, borderwidth=3, bg="#8E44AD", fg="#ecf0f1")
#         self.restart_btn.pack(side="top")

#     def create_game_board(self):
#         frame = tk.Frame(self.root, bg='#ecf0f1')
#         frame.pack()

#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col] = tk.Button(frame, text="", font=("Arial", 40), width=6, height=2,
#                                                    command=lambda row=row, col=col: self.next_turn(row, col), bg="#8E44AD", fg="#ecf0f1")
#                 self.buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

#     def new_game(self):
#         for row in range(3):
#             for col in range(3):
#                 self.buttons[row][col]["text"] = ""
#                 self.buttons[row][col].config(bg="#8E44AD")

#         self.turn_label["text"] = f"{self.current_player}'s Turn"
#         self.current_player = self.players[0]

#     def next_turn(self, row, col):
#         if self.buttons[row][col]['text'] == "" and not self.winner():
#             self.buttons[row][col]['text'] = self.current_player

#             if not self.winner():
#                 self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]
#                 self.turn_label.config(text=f"{self.current_player}'s Turn")
#                 self.computer_move()

#             elif self.winner() == "player":
#                 self.turn_label.config(text=f"{self.players[0]} Wins")
#                 self.player_wins += 1
#                 self.update_scores()
#                 messagebox.showinfo("Game Over", "You win!")

#             elif self.winner() == "computer":
#                 self.turn_label.config(text=f"{self.players[1]} Wins")
#                 self.pc_wins += 1
#                 self.update_scores()
#                 messagebox.showinfo("Game Over", "You Lose!")

#             elif self.winner() == "tie":
#                 self.turn_label.config(text="Tie round, No Winner!")
#                 messagebox.showinfo("Game Over", "It's a tie!")

#     def computer_move(self):
#         if self.current_player == self.players[1]:
#             row, col = self.get_computer_move()
#             self.next_turn(row, col)

#     def get_computer_move(self):
#         empty_cells = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]['text'] == '']
#         return random.choice(empty_cells)

#     def winner(self):
#         for i in range(3):
#             if (self.buttons[i][0]['text'] == self.buttons[i][1]['text'] == self.buttons[i][2]['text'] != ""):
#                 self.highlight_winner_cells(i, 0, i, 1, i, 2)
#                 return "player" if self.buttons[i][0]['text'] == self.players[0] else "computer"

#             if (self.buttons[0][i]['text'] == self.buttons[1][i]['text'] == self.buttons[2][i]['text'] != ""):
#                 self.highlight_winner_cells(0, i, 1, i, 2, i)
#                 return "player" if self.buttons[0][i]['text'] == self.players[0] else "computer"

#         if (self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != ""):
#             self.highlight_winner_cells(0, 0, 1, 1, 2, 2)
#             return "player" if self.buttons[0][0]['text'] == self.players[0] else "computer"

#         if (self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != ""):
#             self.highlight_winner_cells(0, 2, 1, 1, 2, 0)
#             return "player" if self.buttons[0][2]['text'] == self.players[0] else "computer"

#         if not any(self.buttons[i][j]['text'] == "" for i in range(3) for j in range(3)):
#             self.highlight_tie_cells()
#             return "tie"

#         return False

#     def highlight_winner_cells(self, x1, y1, x2, y2, x3, y3):
#         self.buttons[x1][y1].config(bg="#3498DB")
#         self.buttons[x2][y2].config(bg="#3498DB")
#         self.buttons[x3][y3].config(bg="#3498DB")

#     def highlight_tie_cells(self):
#         for i in range(3):
#             for j in range(3):
#                 self.buttons[i][j].config(bg="red")

#     def update_scores(self):
#         self.player_score_label.config(text=f"You: {self.player_wins}")
#         self.pc_score_label.config(text=f"Computer: {self.pc_wins}")


# if __name__ == "__main__":
#     root = tk.Tk()
#     game = TicTacToe(root)
#     root.mainloop()


