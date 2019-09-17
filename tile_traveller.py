# position = 1,1
# while position is not 3,1
#   print valid moves
#   get input
#   is input valid?
#       then update position
# print goodbye message

def validMoves(px, py):
    # skilar streng með valid moves eftir gildum px og py
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
    # biður um input og skilar því í hástöfum
    inp = input("Direction: ")
    return inp.upper()

def inputValid(validMoves, inp):
    # skilar True ef hreyfingin er leyfileg annars False
    validMoves = [x for x in validMoves]
    validMoves = list(filter(lambda x: 65 <= ord(x) <= 90, validMoves))
    return inp in validMoves

def updatePosition(px, py, direction):
    px += 1 if "N" in direction else 0
    px -= 1 if "S" in direction else 0
    py += 1 if "E" in direction else 0
    py -= 1 if "W" in direction else 0
    return px, py


posX = 1
posY = 1

while True:
    if posX == 3 and posY == 1:
        break

