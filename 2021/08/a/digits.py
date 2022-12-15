inputPath = "../input2"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = [i.split(' ') for i in file.read().split('\n')][:-1]
    return data

def countUniqueDigits(digitsList):
    count = 0
    lengths = [2, 3, 4, 7]
    for d in digitsList:
        digits = d[-4:]
        for e in digits:
            if len(e) in lengths:
                count += 1
    return count

def main():
    data = importData(inputPath)
    print(countUniqueDigits(data))
    return 0

if __name__ == "__main__":
    main()
