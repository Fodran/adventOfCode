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
    validRanges = {}
    for line in txtRanges:
        validRanges[line.split(": ")[0]] = line.split(": ")[1].split(" or ")
    for i in validRanges:
        validRanges[i] = [item.split("-") for item in validRanges[i]]
        validRanges[i] = [list(map(int, item)) for item in validRanges[i]]

    return validRanges



def readTicket(txt):
    ticket = [int(i) for i in txt.split(",")]
    return ticket



def validateValue(val, validRanges):

    for ranges in validRanges:
        for vr in validRanges[ranges]:
            if(val >= vr[0] and val <= vr[1]):
                return True
    return False



def validateField(value, vr):
    #print(value, vr)
    #print((value >= vr[0][0] and value <= vr[0][1]) or (value >= vr[1][0] and value <= vr[1][1]))
    return (value >= vr[0][0] and value <= vr[0][1]) or (value >= vr[1][0] and value <= vr[1][1])



def findField(index, validTickets, validRanges):
    fields = []
    for vr in validRanges:
        column = True
        for ticket in validTickets:
            if(not(validateField(ticket[index], validRanges[vr]))):
                column = False
                break
        if column:
            fields.append(vr)
    return fields



def idFields(validTickets, validRanges):
    fieldIndices = {}
    possibleFields = {}

    for i in range(len(validTickets[0])):
        possibleFields[i] = findField(i, validTickets, validRanges)

    for i in range(len(validTickets[0])):
        for index in possibleFields:
            if(len(possibleFields[index]) == 1):
                fieldIndices[possibleFields[index][0]] = index
                key = possibleFields[index][0]
                possibleFields.pop(index)
                for item in possibleFields:
                    possibleFields[item].remove(key)
                break
    
    return fieldIndices



def readYourTicket(txt):
    yourTicket = [int(i) for i in txt[0][13:].split(",")]
    return yourTicket



def calc():
    validRanges, yourTicket, nearbyTickets = importData(path)
    validTickets = []
    counter =1
    validRanges = readRanges(validRanges)
    nearbyTickets = [readTicket(item) for item in nearbyTickets]
    yourTicket = readYourTicket(yourTicket)

    for ticket in nearbyTickets:
        validity = True
        for value in ticket:
            if(not(validateValue(value, validRanges))):
                validity = False
                break
        if validity:
            validTickets.append(ticket)

    fieldIndices = idFields(validTickets, validRanges)
    print(fieldIndices)
    multInd = []
    for field in fieldIndices:
        if "departure" in field:
            multInd.append(fieldIndices[field])

    print(yourTicket)
    for index in multInd:
        print(index, yourTicket[index])
        counter *= yourTicket[index]

    return value


def main():
    print(calc())
    return 0



if __name__ == "__main__":
    main()
