path = "../input"



def importData(path):
    f = open(path, "r")

    data = f.read()
    
    f.close

    validRanges, yourTicket, nearbyTickets = data.split("\n\n")

    validRanges = validRanges.split("\n")
    nearbyTickets = nearbyTickets.split("\n")
    nearbyTickets = nearbyTickets[1:-1]

    return validRanges, [yourTicket], nearbyTickets



def readRanges(txtRanges):
    validRanges = []

    for line in txtRanges:
        validRanges.extend(line.split(": ")[1].split(" or "))

    for i in range(len(validRanges)):
        validRanges[i] = [int(item) for item in validRanges[i].split("-")]

    return validRanges



def readTicket(txt):
    ticket = [int(i) for i in txt.split(",")]
    return ticket



def validateValue(val, validRanges):

    for vr in validRanges:
        if(val > vr[0] and val < vr[1]):
            print("true")
            return True
    return False



def errorRate():
    validRanges, yourTicket, nearbyTickets = importData(path)
    errorRate = 0
    falseValues = []
    
    validRanges = readRanges(validRanges)
    #nearbyTickets = [readTicket(item) for item in nearbyTickets]
    for ticket in nearbyTickets:
        for value in ticket:
            if(not(validateValue(value, validRanges))):
                errorRate += value
                falseValues.append(value)
                break

    return errorRate, sum(falseValues)


def main():
    print(errorRate())
    return 0



if __name__ == "__main__":
    main()
