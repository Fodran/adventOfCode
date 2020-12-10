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
        

def switch(index):
    global instructions

    if(instructions[index][0] == "jmp"):
        instructions[index][0] = "nop"
    elif(instructions[index][0] == "nop"):
        instructions[index][0] = "jmp"



def isLoop():
    global instructions
    global accumulator

    accumulator = 0

    loop = False
    nextStep = 0

    while not(loop):
        instructions[nextStep][2] = True
        nextStep = step(nextStep)
        if(nextStep == len(instructions)):
            return False
        loop = instructions[nextStep][2]

    return True



def initInstructions(data, index):
    global instructions

    instructions = [line + [False] for line in data]
    switch(index)



def findError(data):
    for index in range(len(data)):
        initInstructions(data, index)
        if(not(isLoop())):
            return accumulator
    return 1



def main():
    path = "../input"
    
    print(findError(importData(path)))
    
    return 0



if __name__ == "__main__":
    main()
