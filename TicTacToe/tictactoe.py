board = ["_","_","_",
         "_","_","_",
         "_","_","_"]

currentPlayer = "X"
Winner = None
gameRunning = True

#print board
def printBoard(board):
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("__________")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("__________")
    print(board[6]+" | "+board[7]+" | "+board[8])

#take input
def playerInput(board):
    move = int(input("Enter a number 1-9: "))
    if move >= 1 and move <= 9 and board[move-1] == "_":
        board[move-1] = currentPlayer
    else:
        print("Player is already taken that spot")

def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "_":
        winner = board[1]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True

def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True
    if board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True

def checkTie(board):
    global gameRunning
    if "_" not in board:
        print("Tie")
        printBoard(board)
        gameRunning = False

#switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

def checkWin():
    global gameRunning
    if checkHorizontle(board) or checkRow(board) or checkDiag(board):
        print(f"Winner is {winner}")
        gameRunning = False

while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
