baseBoard = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

def displayBoard(current):
    currentGame = ""
    for row in current:
        row = str(row)
        currentGame = currentGame + row + "\n"
    return currentGame
t = 0
def turn():
    global t
    if t%2==0:
        xTurn()
        winnerCheck("X")
    else:
        oTurn()
        winnerCheck("O")
    t += 1

def xTurn():
    print(displayBoard(current))
    xPlacement = int(input("Player X where do you want to go? : ")) - 1

    if current[(xPlacement//3)][(xPlacement%3)] == xPlacement + 1:
        current[(xPlacement//3)][(xPlacement%3)] = "X"
    else:
        print("Invalid move")
        xTurn()

def oTurn():
    print(displayBoard(current))
    oPlacement = int(input("Player O where do you want to go? : ")) - 1

    if current[(oPlacement//3)][(oPlacement%3)] == oPlacement + 1:
        current[(oPlacement//3)][(oPlacement%3)] = "O"
    else:
        print("Invalid move")
        oTurn()

def winnerCheck(player):
    rowsCheck(player)
    columnsCheck(player)
    diagonalsCheck(player)

def rowsCheck(player):
    global gameFinished
    i = 0
    while i<3:
        if current[i][0] == player and current[i][1] == player and current[i][2] == player:
            gameFinished = True
            print(f"game over {player} Won!")
            print(displayBoard(current))
            sys.exit()
        i=i+1

def columnsCheck(player):
    global gameFinished
    i = 0 
    while i<3:
        if current[0][i] == player and current[1][i] == player and current[2][i] == player:
            gameFinished = True
            print(f"game over {player} Won!")
            print(displayBoard(current))
        i=i+1

def diagonalsCheck(player):
    global gameFinished
    if current[0][0] == player and current[1][1] == player and current[2][2] == player or current[0][2] == player and current[1][1] == player and current[2][0] == player:
        gameFinished = True
        print(f"game over {player} Won!")
        print(displayBoard(current))

current = baseBoard.copy()

gameFinished = False
while gameFinished != True:
    turn()

print("game over")
print(displayBoard(current))