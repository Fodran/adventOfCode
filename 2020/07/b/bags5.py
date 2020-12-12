rules = []



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



def whatsInside(bag):
    listBags = {}
    numBags = 0

    for rule in rules:
        if(rule[0] == bag):
            if(rule[1] == "no other"):
                return 1
            for item in rule[1:]:
                amount, bag = item.split(" ", 1)
                listBags[bag] = int(amount)
    
    print(listBags)
    for bag in listBags:
        print(whatsInside(bag), bag)
        numBags += listBags[bag] * whatsInside(str(bag))

    return numBags



def main():
    global rules
    path = "../input"
    bag = "shiny gold"
    rules = importData(path)

    print(whatsInside(bag))
    return 0



if __name__ == "__main__":
    main()
