path = "../input"
preamble = 25
seq = []
index = 501


def importData(path):
    f = open(path, "r")

    data = [int(line) for line in f]

    f.close()

    return data



def checkNumber(index):
    global seq, preamble
    for i in seq[index - preamble:index]:
        for j in seq[index - preamble:index]:
            if(not(i == j)):
                if(i + j == seq[index]):
                    return True
    return False



def findFirst():
    global seq, preamble
    for index, val in enumerate(seq[preamble:], preamble):
        check = checkNumber(index)
        if(not(check)):
            return check, index, seq[index]



def crack():
    global seq, index
    for numRange in range(index):
        for startRange in range(index - numRange + 1):
            if(sum(seq[startRange:startRange + numRange]) == seq[index]):
                return min(seq[startRange:startRange + numRange]) + max(seq[startRange:startRange + numRange])

    return 0



def main():
    global seq, path, index
    seq = importData(path)
    print(crack())



if __name__ == "__main__":
    main()
