inputPath = "../input"
alphabet = "QWERTYUIOPASDFGHJKLZXCVBNM"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split('\n\n')
        return data



def extractContainers(data):#convert string to a list of lists of containers. Each list corresponds to a pile. First element of a list is the top container of the pile. Last element of a list is the bottom container of a pile.
    tmp = data.split('\n')[:-1]
    containers = [[]]*(len(tmp[0]) // 4 + 1)
    
    for line in tmp:
        for i, c in enumerate(line):
            if c in alphabet:
                if containers[i // 4] == []:
                    containers[i // 4] = [c]
                else:
                    containers[i // 4].append(c)

    return containers



def extractInstructions(data):#convert string to list of instructions in the form a tuple (a, b, c) with a = number of containers to move, b = from which column, c = to which column.
    instructions = []
    tmp = data.split('\n')[:-1]

    for line in tmp:
        instructions.append([int(n) for n in line.split() if n.isdigit()])

    return instructions



def move(nb, dep, arr, containers):#I think a cleaner way would be to only pass the needed columns.
    
    if not containers[dep - 1]:# if departure pile is empty return containers as is
        return containers

    if nb > len(containers[dep - 1]):# if number of containers to move > containers in pile then amount of containers to move becomes amount of containers in pile.
        nb = len(containers[dep - 1])

    containers[arr - 1] = containers[dep - 1][:nb] + containers[arr - 1]
    containers[dep - 1] = containers[dep - 1][nb:]

    return containers



def main():
    strContainers, strInstructions = importData(inputPath)

    containers = extractContainers(strContainers)
    instructions = extractInstructions(strInstructions)

    for i in instructions:
        move(i[0], i[1], i[2], containers)
        for p in containers:
            print(p)

    result = ''
    
    for p in containers:
        result = result + p[0]
        print(p)

    print(result)

    return 0



if __name__ == "__main__":
    main()
