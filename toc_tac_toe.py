import os
import time
from tkinter import *
from tkinter import messagebox

# Global variables for the console version
board = [' ' for _ in range(10)]
player = 1
Win = 1
Draw = -1
Running = 0
Stop = 1
Game = Running
Mark = 'X'

# Console-based Tic-Tac-Toe Functions
def DrawBoard():
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("---|---|---")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("---|---|---")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))

def CheckPosition(x):
    return board[x] == ' '

def CheckWin():
    global Game
    win_conditions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), # Rows
                      (1, 4, 7), (2, 5, 8), (3, 6, 9), # Columns
                      (1, 5, 9), (3, 5, 7)]            # Diagonals

    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            Game = Win
            return
    
    if all(space != ' ' for space in board[1:]):
        Game = Draw
    else:
        Game = Running

def console_game():
    print("Tic-Tac-Toe Game")
    print("Player 1 [X] --- Player 2 [O]\n")
    print("Please Wait...")
    time.sleep(1)

    global player, Game, board
    while Game == Running:
        os.system('cls' if os.name == 'nt' else 'clear')
        DrawBoard()
        if player % 2 != 0:
            print("Player 1's chance")
            Mark = 'X'
        else:
            print("Player 2's chance")
            Mark = 'O'

        try:
            choice = int(input("Enter the position between [1-9] where you want to mark: "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if choice < 1 or choice > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue

        if CheckPosition(choice):
            board[choice] = Mark
            player += 1
            CheckWin()
        else:
            print("Position already occupied. Try again.")

    os.system('cls' if os.name == 'nt' else 'clear')
    DrawBoard()

    if Game == Draw:
        print("Game Draw")
    elif Game == Win:
        player -= 1
        if player % 2 != 0:
            print("Player 1 Won")
        else:
            print("Player 2 Won")

# GUI-based Tic-Tac-Toe Functions
Player1 = 'X'
stop_game = False

b = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
states = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

def clicked(r, c):
    global Player1, stop_game

    if Player1 == "X" and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text="X")
        states[r][c] = 'X'
        Player1 = 'O'

    elif Player1 == 'O' and states[r][c] == 0 and not stop_game:
        b[r][c].configure(text='O')
        states[r][c] = 'O'
        Player1 = "X"

    check_if_win()

def check_if_win():
    global stop_game
    for i in range(3):
        if states[i][0] == states[i][1] == states[i][2] != 0:
            stop_game = True
            messagebox.showinfo("Winner", states[i][0] + " Won!")
            break
        elif states[0][i] == states[1][i] == states[2][i] != 0:
            stop_game = True
            messagebox.showinfo("Winner", states[0][i] + " Won!")
            break
    if not stop_game:
        if all(states[i][j] != 0 for i in range(3) for j in range(3)):
            stop_game = True
            messagebox.showinfo("Tie", "It's a tie!")

def gui_game():
    global b, states, stop_game, Player1
    root = Tk()
    root.title("Tic Tac Toe")
    root.resizable(0, 0)

    for i in range(3):
        for j in range(3):
            b[i][j] = Button(height=4, width=8, font=("Helvetica", "20"), command=lambda r=i, c=j: clicked(r, c))
            b[i][j].grid(row=i, column=j)

    root.mainloop()

# Main Menu to choose the game mode
def main():
    print("Welcome to the Tic-Tac-Toe Game!")
    print("1. Play Console Version")
    print("2. Play GUI Version")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        console_game()
    elif choice == '2':
        gui_game()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        main()

if __name__ == "__main__":
    main()
