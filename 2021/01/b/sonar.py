inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as f:
        data = f.readlines()
    for line in data:
        lines.append(line[:-1])
    return lines

def compareDepths(data):
    counter = 0
    for i in range(len(data) - 3):
        sum1 = data[i] + data[i + 1] + data[i + 2]
        sum2 = data[i + 3] + data[i + 1] + data[i + 2]
        if sum1 < sum2:
            counter += 1
    return counter

def main():
    data = importData(inputPath)
    print(compareDepths(data))
    return 0

if __name__ == "__main__":
    main()
    # the answer is somehow 1266 whereas my script finds 1265 and I can't figure out why
