inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as file:
        data = file.readlines()
    for line in data:
        lines.append(line[:-1])
    return lines

def main():
    return 0

if __name__ == "__main__":
    main()
