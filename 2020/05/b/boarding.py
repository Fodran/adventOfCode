def importData():
    f = open("../input", "r")

    data = []
    for line in f:
        data.append(line)

    f.close()

    return data



def decodeSeat(code):
    rows = range(128)
    columns = range(8)
    for letter in code:
        if(letter == "F"):
            rows = rows[:int(len(rows)/2)]
        elif(letter == "B"):
            rows = rows[int(len(rows)/2):]
        elif(letter == "L"):
            columns = columns[:int(len(columns)/2)]
        else:
            columns = columns[int(len(columns)/2):]
    return [rows[0], columns[0]]



def computeSeatId(coordinates):
    return 8 * coordinates[0] + coordinates[1]



def highestId(seats):
    highestId = 0
    for seat in seats:
        seatId = computeSeatId(decodeSeat(seat))
        if(seatId > highestId):
            highestId = seatId
    return highestId



def findSeat(seats):
    seatIds = [computeSeatId(decodeSeat(seat)) for seat in seats]
    seatIds.sort()

    for seatIdIndex in range(len(seatIds)):
        if(seatIds[seatIdIndex] == seatIds[seatIdIndex + 1] - 2):
             return seatIds[seatIdIndex] + 1



def main():
    #print(highestId(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]))
    print(findSeat(importData()))
    return 0



if __name__ == "__main__":
    main()
