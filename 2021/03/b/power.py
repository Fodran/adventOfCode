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
    else:
        mostBit = 1
    print("noo", numberOfOnes, "len", len(data)/2, "mostBit", mostBit)
    return mostBit

def gasReading(data, gas):
    reading = data.copy()
    for position in range(len(data[0])):
        if len(reading) == 1:
            return reading[0]
        bit = mostBit(reading, position)
        tmpCache = reading.copy()
        reading = select(tmpCache, gas, position, bit)
    print(reading)
    return reading[0]

def select(data, gas, position, mostBit):
    reading = []
    if gas == "o2":
        for line in data:
            if int(line[position]) == mostBit:
                reading.append(line)
    else:
        for line in data:
            if int(line[position]) != mostBit:
                reading.append(line)
    print(reading)
    return reading

def main():
    data = importData(inputPath)
    o2 = gasReading(data, "o2")
    co2 = gasReading(data, "co2")
    print("o2", o2, "co2", co2)
    o2 = int(o2, 2)
    co2 = int(co2, 2)
    print("o2", o2, "co2", co2)
    print("power : ", o2 * co2)
    return 0

if __name__ == "__main__":
    main()
