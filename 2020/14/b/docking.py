path = "../input"



def importData(path):
    f = open(path, "r")
    
    data = [line.replace("\n", "") for line in f]

    f.close()

    return data



def readInstruction(line):
    if(line[:3] == "mem"):
        addr = int(line[4:].split("]")[0])
        value = int(line[4:].split("=")[1])
        #print("addr: ", addr, "; value: ", value)
        return addr, value
    else:
        mask = line[7:]
        #print("mask: ", mask)
        return "mask", mask



def applyMask(addr, mask):
    addrBits = format(addr, "036b")
    addresses = []
    addrTemplate = ""

    #print("addr: ", addr, "is: ", addrBits, "in bits")

    for index, bit in enumerate(mask):
        if(not(bit == "X")):
            addrTemplate += str(int(bit) or int(addrBits[index]))
        else:
            addrTemplate += "X"

    #print("template: ", addrTemplate)
    if(addrTemplate[0] == "X"):
        addresses = ["0", "1"]
        #print(addresses)
    else:
        addresses = [addrTemplate[0]]
        #print(addresses)

    for bit in addrTemplate[1:]:
        #print("bit: ", bit)
        if(bit == "X"):
            #print("addresses: ", addresses)
            tmpAddresses = []
            for address in addresses:
                #print("1: ", address, "; 2: ", (address + "0"))
                tmpAddresses.append(address + "0")
                tmpAddresses.append(address + "1")
            addresses = tmpAddresses[:]
            #print("addresses 1: ", addresses)
        else:
            #print("addresses: ", addresses)
            tmpAddresses = []
            for address in addresses:
                #print("1: ", address, "; 2: ", (address + bit))
                tmpAddresses.append(address + bit)
            addresses = tmpAddresses[:]
            #print("addresses 2: ", addresses)
    
    #print("addresses: ", addresses)
    for address in addresses:
        #print("address: ", address)
        address = int(address, 2)
        #print("address: ", address)
    return addresses



def followInstructions(instructions):
    memory = {}
    mask = "" 

    for line in instructions:
        instruction = readInstruction(line)

        #print("instruction: ", instruction)

        if(instruction[0] == "mask"):
            mask =  instruction[1]
        else:
            for addr in applyMask(instruction[0], mask):
                memory[addr] = instruction[1]

    #print("memory: ", memory)
    return memory



def sumValue():
    count = 0
    memory = followInstructions(importData(path))
    #print("memory2: ", memory)
    for addr in memory:
        count += memory[addr]
        #print("addr: ", addr, "; value: ", memory[addr], "; count: ", count)

    return count



def main():
    print(sumValue())
    return 0



if __name__ == "__main__":
    main()
