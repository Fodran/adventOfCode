inputPath = "../input"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = file.read()
    lines = data.split('\n')[:-1]
    return lines

def main():
    return 0

if __name__ == "__main__":
    main()
