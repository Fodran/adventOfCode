inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        elves = (file.read()+"\n").split("\n\n")[:-1]
        return elves

def calcElfCal(elf):
    cals = [int(c) for c in elf.split("\n")]
    cals = sum(cals)
    return cals

def main():
    elves = importData(inputPath)
    cals = []
    for elf in elves:
        cals.append(calcElfCal(elf))
    sum = 0
    sum += cals.pop(cals.index(max(cals)))
    sum += cals.pop(cals.index(max(cals)))
    sum += cals.pop(cals.index(max(cals)))
    print(sum)
    return 0

if __name__ == "__main__":
    main()
