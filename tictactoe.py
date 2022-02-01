from pickletools import TAKEN_FROM_ARGUMENT1
import random
import time

grid = [[" "," "," "],[" "," "," "],[" "," "," "]]
taken = []
takenO = []
takenX = []
valid = [1,2,3,4,5,6,7,8,9]
def showGrid():
    for row in range(0,3):
        print(grid[row])

def posOnGrid(n, symbol):
    if n in [1,2,3]:
        grid[0].pop(n-1)
        grid[0].insert(n-1, symbol)
        return True
    elif n in [4,5,6]:
        grid[1].pop(n-4)
        grid[1].insert(n-4, symbol)
        return True
    elif n in [7,8,9]:
        grid[2].pop(n-7)
        grid[2].insert(n-7, symbol)
        return True
    else:
        return False

def checkWin():
    if (1 in takenO and 2 in takenO and 3 in takenO) or (4 in takenO and 5 in takenO and 6 in takenO) or (7 in takenO and 8 in takenO and 9 in takenO) or (1 in takenO and 4 in takenO and 7 in takenO) or (2 in takenO and 5 in takenO and 8 in takenO) or (3 in takenO and 6 in takenO and 9 in takenO) or (1 in takenO and 5 in takenO and 9 in takenO) or (3 in takenO and 5 in takenO and 7 in takenO):
        return True, "O"
    elif (1 in takenX and 2 in takenX and 3 in takenX) or (4 in takenX and 5 in takenX and 6 in takenX) or (7 in takenX and 8 in takenX and 9 in takenX) or (1 in takenX and 4 in takenX and 7 in takenX) or (2 in takenX and 5 in takenX and 8 in takenX) or (3 in takenX and 6 in takenX and 9 in takenX) or (1 in takenX and 5 in takenX and 9 in takenX) or (3 in takenX and 5 in takenX and 7 in takenX):
        return True, "X"
    else:
        return False, None

def makeMove():
    desiredPos = random.randint(1,9)
    if desiredPos not in taken and desiredPos in valid:
        taken.append(desiredPos)
        takenX.append(desiredPos)
        placed = posOnGrid(desiredPos, "X")
        if not placed:
            makeMove()
    else:
        makeMove()

won = False
winner = ""
while not won:
    showGrid()
    won, winner = checkWin()
    if won: break

    pos = int(input("\nWhere do you want to go? (1-9): "))
    if pos not in taken and pos in valid:
        taken.append(pos)
        takenO.append(pos)
        posOnGrid(pos, "O")
        time.sleep(1)        
        makeMove()
    else:
        print("Please enter a number in the valid range.")

if winner == "O":
    print("You won!")
elif winner == "X":
    print("You lost!")