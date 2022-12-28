inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = [l[:-1] for l in file.readlines()]

    return data



def readCommands(data):
    currentPath = []
    dirSizes = {}
    deleteFolders = []
    maxSpace = 70000000
    unusedSpace = 0
    space2free = 0

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

    unusedSpace = 70000000 - dirSizes['/']
    space2free = 30000000 - unusedSpace #can be shortened to space2free = dirSizes['/'] - 40000000
    
    for d in dirSizes:
        if dirSizes[d] >= space2free:
            deleteFolders.append(dirSizes[d])

    print(min(deleteFolders))

    return 0 



def main():
    data =importData(inputPath)

    readCommands(data)

    return 0

if __name__ == "__main__":
    main()
