def importData():
    f = open("input", "r")
    
    tableInput = []

    for line in f:
        tableInput.append(line[0: -1])
    
    return tableInput



def isThereATree(posX, posY, treeMap):
    mapWidth = len(treeMap[0])
    #print(treeMap[posX][(posY - 1) % mapWidth])
    if(treeMap[posX][posY % mapWidth] == "#"):
        return True
    return False



def treeCount(slope, treeMap):
    posX = 0
    posY = 0
    counter = 0

    while(posX < len(treeMap)):
        if(isThereATree(posX, posY, treeMap)):
            counter += 1
        
        posX += slope[0]
        posY += slope[1]
    return counter



def main():
    print(treeCount([1, 3], importData()))
    return 0



if __name__ == "__main__":
    main()
