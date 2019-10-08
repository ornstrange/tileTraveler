from random import seed, choice

WIN_XY = (3,1)
LEVER_XY = [(1,2),(2,2),(3,2),(2,3)]

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


def random_direction():
    # Returns a random direction and prints it out
    _choice = choice(["N", "E", "S", "W"])
    print(f"Direction: {_choice.lower()}")
    return _choice


def random_lever_pull():
    # returns a Y or N and prints it out
    _choice = choice(["Y", "N"])
    print(f"Pull a lever (y/n): {_choice.lower()}")
    return _choice


while True:
    # initialize variables
    posX, posY = 1, 1
    coins, moves = 0, 0

    seed_int = int(input("Input seed: "))
    seed(seed_int)

    while True:
        valid_moves = validMoves(posX, posY)
        print("You can travel:", valid_moves)

        user_input = random_direction()

        if inputValid(valid_moves, user_input):
            posX, posY = updatePosition(posX, posY, user_input)
            if (posX, posY) == WIN_XY:
                print(f"Victory! Total coins {coins}. Moves {moves}.")
                break
            elif (posX, posY) in LEVER_XY:
                pull_lever = random_lever_pull()
                if (pull_lever.upper() == "Y"):
                    coins += 1
                    print(f"You received 1 coin, your total is now {coins}.")
        else:
            print("Not a valid direction!")
        moves += 1
    play_again = input("Play again (y/n): ")
    if play_again.upper() != "Y": # quit if play_again is not Y
        break

