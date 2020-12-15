startingNumbers = [2, 0, 1, 7, 4, 14, 18]
#startingNumbers = [0,3,6]


def calcNext(numList):
    last = numList[-1]

    if(not(last in numList[:-1])):
        print(0)
        return 0

    print(numList[::-1].index(last, 1))
    return numList[::-1].index(last, 1)



def play(turns):
    global startingNumbers
    turn = len(startingNumbers)
    
    while turn < turns:
        numList = startingNumbers[:]
        startingNumbers.append(calcNext(numList))
        turn = len(startingNumbers)

    return startingNumbers[-1]



def main():
    print(play(2020))
    return 0



if __name__ == "__main__":
    main()
