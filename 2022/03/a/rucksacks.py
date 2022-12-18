inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split("\n")[:-1]
    return data

#returns item that is in both compartments and returns it
def findItem(ruck):
    c1 = ruck[:int((len(ruck)/2))]
    c2 = ruck[(int(len(ruck)/2)):]

    for letter in c1:
        if c2.find(letter) != -1:
            return letter
    return -1

def letterPriority(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = letters.index(letter) + 1
    return priority

def main():
    data = importData(inputPath)
    totalPriority = 0

    for ruck in data:
        totalPriority += letterPriority(findItem(ruck))

    print(totalPriority)
    return 0

if __name__ == "__main__":
    main()
