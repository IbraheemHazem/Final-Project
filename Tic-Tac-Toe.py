import tkinter as tk
from tkinter import messagebox
import random
import glob


files = glob.glob(r"D:\Coding\Almadrasa\Final Project\*")
print(files)


root = tk.Tk()
root.title("Tic-Tac-Toe game")
root.configure(bg='#D7BDE2')
# root.iconbitmap("TicTacToe.ico")



pcwins = 0
playerwins = 0

buttons = [ 
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

players = ["X", "O"]
player = random.choice(players)
player = players[0]



def NextTurn(row, col):
    global player, pcwins, playerwins
    if buttons[row][col]['text'] == "" and Winner() == False:
        if player == players[0]:
            buttons[row][col]['text'] = player

            if Winner() == False:
                player = players[1]
                label.config(text=f"{players[1]}'s Turn")
                computer_move()

            elif Winner() == True:
                label.config(text=f"{players[0]} Wins")
                playerwins += 1
                myScore.config(text=f"You: {playerwins}")
                messagebox.showinfo("Game Over", "You win!")

            elif Winner() == "tie":
                label.config(text="Tie round, No Winner!")
                messagebox.showinfo("Game Over", "It's a tie!")

        elif player == players[1]:
            buttons[row][col]['text'] = player

            if Winner() == False:
                player = players[0]
                label.config(text=f"{players[0]}'s Turn")

            elif Winner() == True:
                label.config(text=f"{players[1]} Wins")
                pcwins += 1
                myScore2.config(text=f"Computer: {pcwins}")
                messagebox.showinfo("Game Over", "You Lose!")


def computer_move():
    global player
    if player == players[1]:
        row, col = get_computer_move()
        NextTurn(row, col)

        

def get_computer_move():
    empty_cells = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]['text'] == '']
    return random.choice(empty_cells)

def IsEmptySpaces():
    Occupied = 9
    for row in range(3):
        for col in range(3):
            if buttons[row][col]["text"] != "":
                Occupied -= 1
    if Occupied == 0:
        return False
    else:
        return True
    


def Winner():
# horizontal winning 
    for row in range(3):
        if player == players[0] and buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg= "#3498DB")
            buttons[row][1].config(bg= "#3498DB")
            buttons[row][2].config(bg= "#3498DB")
            return True

        elif player == players[1] and buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg= "cyan")
            buttons[row][1].config(bg= "cyan")
            buttons[row][2].config(bg= "cyan")

            return True
# vertical winning 
    for col in range(3):    
        if player == players[0] and buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg= "#3498DB")
            buttons[1][col].config(bg= "#3498DB")
            buttons[2][col].config(bg= "#3498DB")
            return True
        


        if player == players[1] and buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != "":
            buttons[0][col].config(bg= "cyan")
            buttons[1][col].config(bg= "cyan")
            buttons[2][col].config(bg= "cyan")
            return True
        

# First diagonal winning
    if player == players[0] and buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg= "#3498DB")
        buttons[1][1].config(bg= "#3498DB")
        buttons[2][2].config(bg= "#3498DB")
        return True



    elif player == players[1] and buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg= "cyan")
        buttons[1][1].config(bg= "cyan")
        buttons[2][2].config(bg= "cyan")
        return True
    

# Second diagonal winning
    if player == players[0] and buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg= "#3498DB")
        buttons[1][1].config(bg= "#3498DB")
        buttons[2][0].config(bg= "#3498DB")
        return True
    
    elif player == players[1] and buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg= "cyan")
        buttons[1][1].config(bg= "cyan")
        buttons[2][0].config(bg= "cyan")
        return True




    if IsEmptySpaces() == False:
        for row in range(3):
            for col in range(3):
                buttons[row][col].config(bg= "red")
        return "tie"
    
    else:
        return False
    

def NewGame():
    global player
    global players
    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""
            buttons[i][j].config(bg="#8E44AD")
            label["text"] = f"{player}'s Turn"
            player = players[0]





myScore = tk.Label(root, text=f"You: {playerwins}", font=("Arial", 20), bg= "#3498DB")
myScore.pack(anchor= "center")

myScore2 = tk.Label(root, text=f"Computer: {pcwins}", font=("Arial", 20), bg= "cyan")
myScore2.pack(anchor= "center")

label = tk.Label(root, text=(f"{player}'s Turn"), font=("Arial", 40), bg= "#D7BDE2")
label.pack(side= "top")

restartBtn = tk.Button(root, text="Restart",font=("Arial", 15), padx=45, pady=15, command=NewGame, borderwidth=3, bg= "#8E44AD",fg= "#000000")
restartBtn.pack(side="top")

frame = tk.Frame(root)
frame.pack()

exit_button = tk.Button(root, text= "Exit", command= root.destroy, bg= "red", font=("Arial", 15), width=15, height=2, fg="#ecf0f1") 
exit_button.pack(side="bottom", padx=10)

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(frame, text="",font=("Arial", 40),width= 6, height= 2, command=lambda row=row, col= col: NextTurn(row, col), bg="#8E44AD")
        buttons[row][col].grid(row= row, column= col)

root.mainloop()




