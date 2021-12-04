inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as f:
        data = f.readlines()
    for line in data:
        lines.append(line[:-1])
    return lines

def plan(data):
    depth = 0
    horizon = 0
    for line in data:
        command, value = line.split(' ')
        if command == "forward":
            horizon += int(value)
        elif command == "down":
            depth += int(value)
        else:
            depth -= int(value)
    return depth * horizon

def main():
    data = importData(inputPath)
    print(plan(data))
    return 0

if __name__ == "__main__":
    main()
