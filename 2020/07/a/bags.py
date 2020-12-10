def importData(path):
    f = open(path, "r")

    data = [line.split("contain") for line in f]

    f.close()

    return data



def countBags(rules):
    outerBags = []
    newBags = True

    for line in rules:
        outerColor = line[0].replace(" bags ", "")
        innerColors = line[1]
        if("shiny gold" in innerColors):
            outerBags.append(outerColor)
    
    while newBags:
        newBags = False
        for line in rules:
            outerColor = line[0].replace(" bags ", "")
            innerColors = line[1]

            for bagColor in outerBags:
                if(bagColor in innerColors and not (outerColor in outerBags)):
                    outerBags.append(outerColor)
                    newBags = True
    return len(set(outerBags))



def main():
    path = "../input"
    print(countBags(importData(path)))
    return 0



if __name__ == "__main__":
    main()
