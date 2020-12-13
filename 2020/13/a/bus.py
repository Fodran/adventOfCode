path = "../input"



def importData(path):
    f = open(path, "r")

    data = [int(f.readline().replace("\n", ""))]

    data += [int(number) for number in f.readline().split(",") if(not(number == "x"))]

    f.close()

    return data



def nextDeparture(busID, earliestTimestamp):
    return busID * (earliestTimestamp // busID + 1)



def earliestDeparture(timetable):
    earliestTimestamp = timetable[0]
    busIDs = timetable[1:]
    nextBus = [busIDs[0], nextDeparture(busIDs[0], earliestTimestamp)]

    for busID in busIDs:
        nextTime = nextDeparture(busID, earliestTimestamp)
        if(nextTime < nextBus[1]):
            nextBus = [busID, nextTime]

    return nextBus



def calcFlag():
    timetable = importData(path)
    nextBus = earliestDeparture(timetable)

    return nextBus[0] * (nextBus[1] - timetable[0])



def main():
    print(calcFlag())
    return 0



if __name__ == "__main__":
    main()
