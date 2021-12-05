inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as file:
        data = file.readlines()
    for line in data:
        lines.append(line[:-1])
    return lines

def countGamma(data):
    gammaCounter = ''
    for i in range(len(data[0])):
        numberOfOnes = 0
        for j in range(len(data)):
            numberOfOnes += int(data[j][i])
        if numberOfOnes < len(data)/2:
            gammaCounter += '0'
        else:
            gammaCounter += '1'
    return gammaCounter

def inverter(binaryCounter):
    inverted = ''
    for i in binaryCounter:
        if i == '0':
            inverted += '1'
        else:
            inverted += '0'
    return inverted

def main():
    data = importData(inputPath)
    gamma = countGamma(data)
    epsilon = inverter(gamma)
    print("power : " + str(int(gamma, 2) * int(epsilon, 2)))
    return 0

if __name__ == "__main__":
    main()
