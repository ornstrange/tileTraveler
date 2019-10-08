from random import seed, choice

def validMoves(px, py):
    # skilar streng með valid moves eftir gildum player x og player y
    if px in [1, 2, 3] and py == 1:
        return "(N)orth."
    if px == 1 and py == 2:
        return "(N)orth or (E)ast or (S)outh."
    if px == 1 and py == 3:
        return "(E)ast or (S)outh."
    if px == py:
        return "(S)outh or (W)est."
    if px == 2 and py == 3:
        return "(E)ast or (W)est."
    if px == 3 and py == 2:
        return "(N)orth or (S)outh."

def getInput():
    # asks for a direction, returns it uppercase
    inp = input("Direction: ")
    return inp.upper()

def inputValid(validMoves, inp):
    # returns if the input is a valid move
    validMoves = [x for x in validMoves]
    validMoves = list(filter(lambda x: 65 <= ord(x) <= 90, validMoves))
    return inp in validMoves

def updatePosition(px, py, direction):
    # updates position from direction
    py += 1 if "N" in direction else 0
    py -= 1 if "S" in direction else 0
    px += 1 if "E" in direction else 0
    px -= 1 if "W" in direction else 0
    return px, py

while True:
    posX = 1
    posY = 1
    coins = 0
    moves = 0
    seed_int = int(input("Input seed: "))
    seed(seed_int)
    while True:
        print("You can travel:", validMoves(posX, posY))
        #user_input = getInput()
        user_input = choice(["N", "E", "S", "W"])
        print(f"Direction: {user_input.lower()}")
        moves += 1
        if inputValid(validMoves(posX, posY), user_input):
            posX, posY = updatePosition(posX, posY, user_input)
            if posX == 3 and posY == 1:
                print(f"Victory! Total coins {coins}. Moves {moves}.")
                break
            elif posY == 2 or (posX == 2 and posY == 3):
                #pull_lever = input("Pull a lever (y/n): ")
                pull_lever = choice(["Y", "N"])
                print(f"Pull a lever (y/n): {pull_lever.lower()}")
                if (pull_lever.upper() == "Y"):
                    coins += 1
                    print(f"You received 1 coin, your total is now {coins}.")
        else:
            print("Not a valid direction!")
    play_again = input("Play again (y/n): ")
    if play_again.upper() != "Y":
        break

