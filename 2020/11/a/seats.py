import copy



path = "../input2"
seatsMap = []



def importData(path):
    f = open(path, "r")

    data = [list(line.replace("\n", "")) for line in f]

    f.close()

    return data



def checkNeighbours(seatX, seatY):
    rangeX = [-1, 0, 1]
    rangeY = [-1, 0, 1]
    occupiedCount = 0

    if(seatX == 0):
        rangeX.remove(-1)
    elif(seatX == len(seatsMap) - 1):
        rangeX.remove(1)
    if(seatY == 0):
        rangeY.remove(-1)
    elif(seatY == len(seatsMap[0]) - 1):
        rangeY.remove(1)

    for x in rangeX:
        for y in rangeY:
            if(not(x == 0 and y == 0)):
                if(seatsMap[seatX + x][seatY + y] == "#"):
                    occupiedCount += 1

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
