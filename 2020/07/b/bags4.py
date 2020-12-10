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


def listInnerBags(rules, bag, coeff):
    for rule in rules:
        if(rule[0] == bag):
            if(not(rule[1] == "no other")):
                if isinstance(rule[1], list):
                    for item in rule[1]:
                        amount = int(item.split(" ", 1)[0]) * coeff
                        color = item.split(" ", 1)[1]
                        colors[color] = amount
                else:
                    amount = int(rule.split(" ", 1)[0]) * coeff
                    color = rule.split(" ", 1)[1]
                    colors[color] = amount
            else:
                return 1

    return colors



def main():
    path = "../input"
    bag = "shiny gold"
    print(listInnerBags(importData(path), bag, 1))
    return 0



if __name__ == "__main__":
    main()
