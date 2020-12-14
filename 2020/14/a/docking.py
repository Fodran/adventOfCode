path = "../input"



def importData(path):
    f = open(path, "r")
    
    data = [line.replace("\n", "") for line in f]

    f.close()

    return data



def convertMask(mask):
    conv = {}

    for index, value in enumerate(mask):
        if(not(value == "X")):
            conv[index] = value

    print("converted mask: ", conv)

    return conv



def readInstruction(line):
    if(line[:3] == "mem"):
        addr = int(line[4:].split("]")[0])
        value = int(line[4:].split("=")[1])
        print("addr: ", addr, "; value: ", value)
        return addr, value
    else:
        mask = convertMask(line[7:])
        print("mask: ", mask)
        return "mask", mask



def applyMask(value, mask):
    newValue = format(value, "036b")
    
    print("value: ", value, "; newValue: ", newValue, "; mask: ", mask)
    for i in mask:
        newValue = newValue[:i] + mask[i] + newValue[i + 1:]

    print("new value: ", newValue, "; int: ", int(newValue, 2))

    return int(newValue, 2)



def followInstructions(instructions):
    memory = {}
    mask = {}

    for line in instructions:
        instruction = readInstruction(line)

        print("instruction: ", instruction)

        if(instruction[0] == "mask"):
            mask = instruction[1]
        else:
            memory[instruction[0]] = applyMask(instruction[1], mask)

    print("memory: ", memory)
    return memory



def sumValue():
    count = 0
    memory = followInstructions(importData(path))
    print("memory2: ", memory)
    for addr in memory:
        count += memory[addr]
        print("addr: ", addr, "; value: ", memory[addr], "; count: ", count)

    return count



def main():
    print(sumValue())
    return 0



if __name__ == "__main__":
    main()
