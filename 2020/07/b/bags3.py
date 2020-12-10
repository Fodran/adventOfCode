def importData(path):
    f = open(path, "r")

    data = [line for line in f]

    f.close()

    output = sanitize(data)

    return output



def sanitize(data):
    output = []

    for line in data:
        outerColor = line.split(" contain ")[0].replace(" bags", "")
        innerColors = [x.strip() for x in line.split(" contain ")[1].replace(" bags", "").replace(" bag", "").replace(".\n", "").split(", ")]
        output.append([outerColor] + innerColors)

    return output


def listInnerBags(rule, coeff):
    colors = {}
    
    if(not(rule == "no other")):
        if isinstance(rule, list):
            for item in rule:
                amount = int(item.split(" ", 1)[0]) * coeff
                color = item.split(" ", 1)[1]
                colors[color] = amount
        else:
            amount = int(rule.split(" ", 1)[0]) * coeff
            color = rule.split(" ", 1)[1]
            colors[color] = amount

    return colors



def countBags(rules):
    bags = {}
    newBags = True

    for line in rules:
        if(line[0] == "shiny gold"):
            bags.update(listInnerBags(line[1:], 1))
            break
   
    while newBags:
        newBags = False
        bagsToAdd = {}
        for bag in bags:
            for line in rules:
                if(bag in line[0]):
                    if(not(line[1] == "no other")):
                        innerColors = listInnerBags(line[1], bags[bag])
                        if(not(innerColors == {})):
                            for color in innerColors:
                                bagsToAdd[color] = innerColors[color]
                            newBags = True

        for bag in bagsToAdd:
            if bag in bags:
                bags[bag] += bagsToAdd[bag]
            else:
                bags[bag] = bagsToAdd[bag]

        print("pass")
        bags.update(bagsToAdd)

    return bags



def main():
    path = "../input"
    print(countBags(importData(path)))
    return 0



if __name__ == "__main__":
    main()
