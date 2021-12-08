import numpy as np
inputPath = "../input"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = [int(i) for i in file.read().split(',')]
    return data

def optimalPosition(posList):
    minP = min(posList)
    maxP = max(posList)
    fuel = []
    for i in range(minP, maxP + 1):
        fuel.append(calcFuel(i, posList))
    pos = np.argmin(fuel) + minP
    fuel = calcFuel(pos, posList)
    return pos, fuel

def calcFuel(pos, posList):
    fuelCount = 0
    for p in posList:
        fuelCount += arSum(abs(pos - p))
    return fuelCount

def arSum(nb):
    return (nb + 1) * nb / 2

def main():
    data = importData(inputPath)
    print(data)
    fuel = optimalPosition(data)
    print(fuel)
    return 0

if __name__ == "__main__":
    main()
