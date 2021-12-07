inputPath = "../input"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = [int(i) for i in file.read().split(',')]
    return data

def nextFish(fishCounter):
    if fishCounter == 0:
        return [6, 8]
    return [fishCounter - 1]

def oneTurn(fishList):
    newFishList = []
    for f in fishList:
        newFishList.extend(nextFish(f))
    return newFishList

def playTurns(nb, fishList):
    newFishList = fishList.copy()
    for i in range(nb):
        newFishList = oneTurn(newFishList)
    return newFishList

def main():
    fishList = importData(inputPath)
    nbTurns = 80
    print(fishList)
    print(len(playTurns(nbTurns, fishList)))
    return 0

if __name__ == "__main__":
    main()
