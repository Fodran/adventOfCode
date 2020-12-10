def importData(path):
    f = open(path, "r")

    data = [line.replace("bags", "").replace("bag", "").strip().split(" contain") for line in f]

    f.close()

    return data



def listInsideBags(innerRule, coeff):
    colors = {}
    individualColors = innerRule[:-1].split(", ")
    
    for color in individualColors:
        colorEntry = color.split(" ", 1)
        
        colors[colorEntry[1].strip()] = int(colorEntry[0]) * coeff
    print(colors) 
    return colors



def countBags(rules):
    innerBags = {}
    newBags = True

    for line in rules:
        outerColor = line[0].strip()
        innerRules = line[1].strip()
        if("shiny gold" in outerColor):
            innerBags.update(listInsideBags(innerRules, 1))

    while newBags:
        newBags = False
        tmpDict = {}
        for bag in innerBags.copy():
            for line in rules:
                outerColor = line[0].strip()
                innerRule = line[1].strip()

                if(bag in outerColor):
                    if(not("no other bags" in innerRule)):
                        newBags == True
                        tmpDict.update(listInsideBags(innerRules, innerBags[bag]))
        innerBags.update(tmpDict)

    return innerBags
"""
    while newBags:
        newBags = False
        for line in rules:
            outerColor = line[0].strip()
            innerRule = line[1].strip()

            if(outerColor in innerBags):
                innerColors = listInsideBags(innerRule)
                print(innerColors)
                for color in innerColors:
                    if(not(color in innerBags)):
                        innerBags[color[0]] = color[1] * innerBags[outerColor]
                        if(innerColors[0]
                        newBags = True
                        print(innerBags)
"""




def main():
    path = "../input"
    print(countBags(importData(path)))
    return 0



if __name__ == "__main__":
    main()
