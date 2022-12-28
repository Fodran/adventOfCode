import copy



path = "../input"
currentState = []


def importData():
    with open(path) as f:
        data = f.read()
    
    output = data.split("\n")
    return output



def isCellEmpty(x, y, z):
    return "." == currentState[x][y][z]
    


def isPlaneEmpty(const, value):
    
    if const == "x":
        for y in range(len(currentState[0])):
            for z in range(len(currentState[0][0])):
                if(not(isCellEmpty(value, y, z))):
                    return False

    elif const == "y":
        for x in range(len(currentState)):
            for z in range(len(currentState[0][0])):
                if(not(isCellEmpty(x, value, z))):
                    return False

    elif const == "z":
        for x in range(len(currentState)):
            for y in range(len(currentState[0])):
                if(not(isCellEmpty(x, y, value))):
                    return False

    return True


def addZ(index):
    for x in range(len(currentState)):
        for y in range(len(currentState[0])):
            # insert ? append ? numpy ?
            currentState[x][y][z]
    return 0


    
def addY(index):
    # TO DO
    for x in range(len(currentState)):
        for z in range(len(currentState[0][0])):
            # insert ? append ? numpy ?
            currentState[x][index][z].
    return 0



def addX(index):
    # TO DO
    for y in range(len(currentState[0])):
        for z in range(len(currentState[0][0])):
            # insert ? append ? maybe use numpy arrays ??
            currentState[index][y][z]
    return 0



def calcNeighbours(x, y, z):
    count = 0
    rangeX = [-1, 0, 1]
    rangeY = [-1, 0, 1]
    rangeZ = [-1, 0, 1]

    for dx in rangeX:
        for dy in rangeY:
            for dz in rangeZ:
                if(not(z == 0 and x == 0 and y == 0)):
                    if(not(isCellEmpty(x + dx, y + dy, z + dz))):
                        count += 1
    return count



def cycle(state):
    # TO DO
    numLoops = 6
    tmpState = copy.deepcopy(currentState)

    if isPlaneEmpty(
    for i in range(numLoops):
        
    return newState



def main():
    return 0



if __name__ == "__main__":
    main()
