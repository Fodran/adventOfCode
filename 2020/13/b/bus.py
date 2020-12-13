path = "../input"



def importData(path):
    f = open(path, "r")

    f.readline()
    data = [int(number) if(not(number == "x")) else number for number in f.readline().split(",")]
    #data = [1789,37,47,1889]
    output = [[int(number), data.index(number)] for number in data if(not(number == "x"))]

    f.close()

    return output



def isBus(busID, timestamp):
    return timestamp % busID == 0



def findT(timetable):
    startTime = 100000000000000
    maxStep = max(timetable, key = lambda x: x[0])
    print(maxStep)
    maxValue = maxStep[0]
    maxIndex = maxStep[1]

    t = (startTime//maxValue + 1) * maxValue - maxIndex
    while True:
        if checkT(t, timetable):
            return t
        t += maxValue
        print(t)



def checkT(t, timetable):
    for bus in timetable:
        if(not(isBus(bus[0], t + bus[1]))):
            return False

    return True



def main():
    print(findT(importData(path)))
    return 0



if __name__ == "__main__":
    main()
