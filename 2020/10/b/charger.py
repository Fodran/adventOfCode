path = "../input"



def importData(path):
    f = open(path, "r")

    data = [int(line) for line in f]

    f.close()

    return data



def originalChain(data):
    chain = sorted(data) 
    chain.insert(0, 0)
    chain.append(chain[-1] + 3)
    return chain



def chainCombinations(originalChain):
    counter = 1
    pathsCounter = {}

    for i in originalChain:
        pathsCounter[i] = 0
    
    pathsCounter[0] = 1

    for i in range(len(originalChain) - 1):
        for j in range(1, 4):
            if(originalChain[i] + j in originalChain):
                pathsCounter[originalChain[i] + j] += pathsCounter[originalChain[i]]
    
    return pathsCounter



def main():
    print(chainCombinations(originalChain(importData(path))))
    return 0



if __name__ == "__main__":
    main()
