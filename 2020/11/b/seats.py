import copy



path = "../input"
seatsMap = []



def importData(path):
    f = open(path, "r")

    data = [list(line.replace("\n", "")) for line in f]

    f.close()

    return data



def checkN(seatX, seatY):
    for x in range(seatX):
        if(seatsMap[seatX - (x + 1)][seatY] == "#"):
            return 1
        if(seatsMap[seatX - (x + 1)][seatY] == "L"):
            return 0
    return 0




def checkS(seatX, seatY):
    height = len(seatsMap) - 1

    for x in range(height - seatX):
        if(seatsMap[seatX  + x + 1][seatY] == "#"):
            return 1
        if(seatsMap[seatX + x + 1][seatY] == "L"):
            return 0
    return 0



def checkW(seatX, seatY):
    for y in range(seatY):
        if(seatsMap[seatX][seatY - (y + 1)] == "#"):
            return 1
        if(seatsMap[seatX][seatY - (y + 1)] == "L"):
            return 0
    return 0



def checkE(seatX, seatY):
    width = len(seatsMap[0]) - 1

    for y in range(width - seatY):
        if(seatsMap[seatX][seatY + y + 1] == "#"):
            return 1
        if(seatsMap[seatX][seatY + y + 1] == "L"):
            return 0
    return 0



def checkNW(seatX, seatY):
    for d in range(min(seatX, seatY)):
        if(seatsMap[seatX - (d + 1)][seatY - (d + 1)] == "#"):
            return 1
        if(seatsMap[seatX - (d + 1)][seatY - (d + 1)] == "L"):
            return 0
    return 0



def checkNE(seatX, seatY):
    width = len(seatsMap[0]) -1

    for d in range(min(seatX, width - seatY)):
        if(seatsMap[seatX - (d + 1)][seatY + d + 1] == "#"):
            return 1
        if(seatsMap[seatX - (d + 1)][seatY + d + 1] == "L"):
            return 0
    return 0



def checkSE(seatX, seatY):
    height = len(seatsMap) - 1
    width = len(seatsMap[0]) - 1

    for d in range(min(height - seatX, width - seatY)):
        if(seatsMap[seatX + d + 1][seatY + d + 1] == "#"):
            return 1
        if(seatsMap[seatX + d + 1][seatY + d + 1] == "L"):
            return 0
    return 0



def checkSW(seatX, seatY):
    height = len(seatsMap) - 1

    for d in range(min(height - seatX, seatY)):
        if(seatsMap[seatX + d + 1][seatY - (d + 1)] == "#"):
            return 1
        if(seatsMap[seatX + d + 1][seatY - (d + 1)] == "L"):
            return 0
    return 0



def checkNeighbours(seatX, seatY):
    occupiedCount = 0

    occupiedCount += checkN(seatX, seatY)
    occupiedCount += checkS(seatX, seatY)
    occupiedCount += checkE(seatX, seatY)
    occupiedCount += checkW(seatX, seatY)
    occupiedCount += checkNE(seatX, seatY)
    occupiedCount += checkNW(seatX, seatY)
    occupiedCount += checkSE(seatX, seatY)
    occupiedCount += checkSW(seatX, seatY)

    return occupiedCount



def switchSeat(seatX, seatY):
    if(seatsMap[seatX][seatY] == "L"):
        if(checkNeighbours(seatX, seatY) == 0):
            return "#"
    if(seatsMap[seatX][seatY] == "#"):
        if(checkNeighbours(seatX, seatY) >= 5):
            return "L"
    return seatsMap[seatX][seatY]



def switchMap():
    global seatsMap
    tmpMap = copy.deepcopy(seatsMap)
    for seatX in range(len(seatsMap)):
        for seatY in range(len(seatsMap[0])):
            tmpMap[seatX][seatY] = switchSeat(seatX, seatY)
    if(tmpMap == seatsMap):
        return False
    seatsMap = copy.deepcopy(tmpMap)
    return True


def printMap(theMap):
    for line in theMap:
        print("".join(line))
    
    print("\n\n\n")


def equilibrium():
    run = True
    while run:
        printMap(seatsMap)
        run = switchMap()



def countOccupied():
    counter = 0
    printMap(seatsMap)
    for row in seatsMap:
        for seat in row:
            if(seat == "#"):
                print(type(seat))
                counter += 1
    
    return counter



def main():
    global seatsMap
    seatsMap = importData(path)
    equilibrium()
    print(countOccupied())
    return 0



if __name__ == "__main__":
    main()
