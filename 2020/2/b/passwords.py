def importData():
    f = open("input", "r")

    tableInput = []

    for line in f:
        tableInput.append(line.split())
        tableInput[-1][0] = tableInput[-1][0].split("-")

    f.close()
    return tableInput



def passVerif(line):
    pos1 = int(line[0][0]) - 1
    pos2 = int(line[0][1]) - 1
    letter = line[1][0]
    password = line[2]

    if((letter == password[pos1]) != (letter == password[pos2])):
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
