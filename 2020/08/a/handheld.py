instructions = []
accumulator = 0


def importData(path):
    f = open(path, "r")

    data = [line[:-1].split(" ") for line in f]

    return data



def step(nextStep):
    global instructions
    global accumulator
    
    command = instructions[nextStep][0]
    value = int(instructions[nextStep][1])

    if(command == "nop"):
        return nextStep + 1
    if(command == "acc"):
        accumulator += value
        return nextStep + 1
    if(command == "jmp"):
        return nextStep + value
        




def findLoop(data):
    global instructions
    global accumulator

    instructions = [line + [False] for line in data]
    accumulator = 0

    loop = False
    nextStep = 0

    while not(loop):
        instructions[nextStep][2] = True
        nextStep = step(nextStep)
        loop = instructions[nextStep][2]

    return accumulator, nextStep, instructions[nextStep]



def main():
    path = "../input"
    
    print(findLoop(importData(path)))
    
    return 0



if __name__ == "__main__":
    main()
