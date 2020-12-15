import datetime



startingNumbers = [2, 0, 1, 7, 4, 14, 18]
#startingNumbers = [3,2,1]


def calcNext(numDict, last, turn):

    if(not(last in numDict)):
        #print(0)
        return 0

    #print(turn - numDict[last])
    return turn - numDict[last]



def play(turns):
    global startingNumbers

    numbers = {}

    for index, num in enumerate(startingNumbers):
        numbers[num] = index + 1

    turn = len(startingNumbers)
    last = startingNumbers[-1]

    while turn < turns:
        previous = last
        last = calcNext(numbers, last, turn)
        numbers[previous] = turn
        turn += 1
        if(turn%500000 == 0 or turn > 29999995 or turn < 10):
            print(turn, previous, last)

    return last



def main():
    begin = datetime.datetime.now()
    print(play(30000000))
    print(datetime.datetime.now() - begin)
    return 0



if __name__ == "__main__":
    main()

