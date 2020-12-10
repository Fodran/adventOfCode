path = "../input"



def importData(path):
    f = open(path, "r")

    data = [int(line) for line in f]

    f.close()

    return data



def chainChargers(data):
    chain = sorted(data) 
    chain.insert(0, 0)
    chain.append(chain[-1] + 3)
    differences = [chain[i + 1] - chain[i] for i in range(len(chain) - 1)]
    diff1 = differences.count(1)
    diff2 = differences.count(2)
    diff3 = differences.count(3)
    return differences, diff1, diff2, diff3



def main():
    results = chainChargers(importData(path))
    print(results[1] * results[3])
    return 0



if __name__ == "__main__":
    main()
