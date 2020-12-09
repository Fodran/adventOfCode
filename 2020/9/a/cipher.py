path = "../input"
preamble = 25
seq = []



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



def main():
    global seq, path
    seq = importData(path)
    print(findFirst())



if __name__ == "__main__":
    main()
