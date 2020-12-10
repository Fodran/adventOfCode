def importData():
    f = open("../input", "r")

    tableInput = []

    for line in f:
        tableInput.append(line.split())
        tableInput[-1][0] = tableInput[-1][0].split("-")

    f.close()
    return tableInput



def letterCounter(letter, word):
    letterCount = 0
    for x in word:
        if letter == x:
            letterCount += 1
    return letterCount



def passVerif(line):
    letterCount = letterCounter(line[1][0], line[2])
    if(letterCount >= int(line[0][0]) and letterCount <= int(line[0][1])):
        return True
    return False



def main():
    data = importData()
    counter = 0

    for line in data:
        if(passVerif(line)):
            counter += 1
    
    print(counter)
    return 0



if __name__ == "__main__":
    main()
