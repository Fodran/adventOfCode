inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as file:
        tmp = file.readlines()
    for line in tmp:
        lines.append(line[:-1])
    return lines

def mostBit(data, position):
    numberOfOnes = 0
    mostBit = -1
    for j in range(len(data)):
        numberOfOnes += int(data[j][position])
    if numberOfOnes < len(data)/2:
        mostBit = 0
    elif numbersOfOnes > len(data)/2:
        mostBit = 1
    else:
        mostBit = 2
    return mostBit

def gasReading(data, gas):
    reading = data.copy()
    for position in range(len(data[0])):
        if len(reading) == 1:
            return reading[0]
        mostBit = mostBit(reading, position)
        if mostBit == 2:
            mostBit = 1 if gas == "o2" else mostBit = 0
        reading = select(reading, position, mostBit)
    return reading

def select(data, position, mostBit):
    reading = []
    for line in data:
        if line[position] == mostBit:
            reading.append(line)
    return reading

def main():
    data = importData(inputPath)
    o2, co2 = findGasRatings(data)
    print("power : " + str(int(gamma, 2) * int(epsilon, 2)))
    return 0

if __name__ == "__main__":
    main()
