xisWinner = False
yisWinner = False
isDraw = False

board = [" " for i in range(1, 10)]

def printBoard():
    print()
    print("|{}|{}|{}|".format(board[0], board[1], board[2]))
    print("|{}|{}|{}|".format(board[3], board[4], board[5]))
    print("|{}|{}|{}|".format(board[6], board[7], board[8]))
    print()

def playerMove(icon):
    if icon == "x":
        number = 1
    elif icon == "o":
        number = 2
    print("Your move player {}".format(number))
    printBoard()
    choice = int(input("Enter the space to put {}:".format(icon)).strip())

    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print("place taken")

def isVictory(icon):
    if(board[0] == icon and board[1] == icon and board[2] == icon) or \
      (board[3] == icon and board[4] == icon and board[5] == icon) or \
      (board[6] == icon and board[7] == icon and board[8] == icon) or \
      (board[0] == icon and board[3] == icon and board[6] == icon) or \
      (board[1] == icon and board[4] == icon and board[7] == icon) or \
      (board[2] == icon and board[5] == icon and board[8] == icon) or \
      (board[0] == icon and board[4] == icon and board[8] == icon) or \
      (board[2] == icon and board[4] == icon and board[6] == icon):
        print("{} wins !!".format(icon))
        return True
    else:
        return False
def is_draw():
    for i in range(1, 10):
        if board[i] == " ":
            return False
            break
    print("Its a draw !!".format(icon))
    return True


while 1:
    playerMove("x")
    if isVictory("x"):
        break
    if is_draw():
        break
    if playerMove("o"):
        break
    if isVictory("o"):
        break
    if is_draw():
        break
