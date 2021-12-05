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
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            counter += 1
    return counter

def main():
    data = importData(inputPath)
    print(compareDepths(data))
    return 0

if __name__ == "__main__":
    main()
    # the answer is somehow 1217 whereas my script finds 1214 (which is +3) and I can't figure out why
