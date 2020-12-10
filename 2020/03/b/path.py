def importData():
    f = open("../input", "r")
    
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
    treeMap = importData()
    counter1 = treeCount([1, 1], treeMap)
    counter2 = treeCount([1, 3], treeMap)
    counter3 = treeCount([1, 5], treeMap)
    counter4 = treeCount([1, 7], treeMap)
    counter5 = treeCount([2, 1], treeMap)
    
    print(counter1)
    print(counter2)
    print(counter3)
    print(counter4)
    print(counter5)


    print(counter1 * counter2 * counter3 * counter4 * counter5)
    return 0



if __name__ == "__main__":
    main()
