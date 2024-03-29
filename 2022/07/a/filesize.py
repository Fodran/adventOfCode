inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = [l[:-1] for l in file.readlines()]

    return data



def findSum(dirDict):
    s = 0
    
    for d in dirDict:
        if dirDict[d] <= 100000:
            s += dirDict[d]
    
    return s



def readCommands(data):
    currentPath = []
    dirSizes = {}

    for line in data:
        if line[:7] == '$ cd ..':
            currentPath.pop()
        elif line[:4] == '$ cd':
            currentPath.append(line[5:])
        elif line[:4] == '$ ls':
            continue
        elif line[:3] == 'dir':
            continue
        else:
            size = int(line.split()[0])

            for i, d in enumerate(currentPath):
                name = ''.join(currentPath[:i + 1])
                dirSizes.setdefault(name, 0)
                dirSizes[name] += size

    print(findSum(dirSizes))

    return 0 



def main():
    data =importData(inputPath)

    readCommands(data)

    return 0

if __name__ == "__main__":
    main()
