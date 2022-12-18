inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split("\n")[:-1]
    return data

#returns item that is in both compartments and returns it
def findItem(r1, r2, r3):
    for letter in r1:
        if r2.find(letter) != -1 and r3.find(letter) != -1:
            return letter
    return -1

def letterPriority(letter):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = letters.index(letter) + 1
    return priority

def main():
    data = importData(inputPath)
    totalPriority = 0
    for i in range(0, len(data), 3):
        totalPriority += letterPriority(findItem(data[i], data[i + 1], data[i + 2]))

    print(totalPriority)
    return 0

if __name__ == "__main__":
    main()
