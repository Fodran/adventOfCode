inputPath = "../input"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = [int(i) for i in file.read().split(',')]
    fDict = {}
    for d in data:
        fDict[d] = fDict.get(d, 0) + 1
    return fDict

def oneTurnOld(fishDict):
    newFishDict = {}
    for f in fishDict:
        if f == 0:
            newFishDict[8] = fishDict[0]
            newFishDict[6] = fishDict[0] + fishDict.get(7, 0)
        elif f == 7:
            pass
        else:
            newFishDict[f - 1] = fishDict[f]
    return newFishDict

def oneTurn(fishDict):
    newFishDict = {}
    newFishDict[0] = fishDict.get(1, 0)
    newFishDict[1] = fishDict.get(2, 0)
    newFishDict[2] = fishDict.get(3, 0)
    newFishDict[3] = fishDict.get(4, 0)
    newFishDict[4] = fishDict.get(5, 0)
    newFishDict[5] = fishDict.get(6, 0)
    newFishDict[6] = fishDict.get(7, 0) + fishDict.get(0, 0)
    newFishDict[7] = fishDict.get(8, 0)
    newFishDict[8] = fishDict.get(0, 0)
    return newFishDict

def playTurns(nb, fishDict):
    newFishDict = fishDict.copy()
    for i in range(nb):
        newFishDict = oneTurn(newFishDict)
    
    return newFishDict

def countFishes(fishDict):
    counter = 0
    for f in fishDict:
        counter += fishDict[f]
    return counter

def main():
    fishDict = importData(inputPath)
    nbTurns = 256
    print(countFishes(playTurns(nbTurns, fishDict)))
    return 0

if __name__ == "__main__":
    main()
