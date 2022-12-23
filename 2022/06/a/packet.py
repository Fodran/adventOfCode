inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read()
        return data



def testCache(cache):

    for i in cache:
        if cache.count(i) != 1:
            return False

    return True



def main():
    sequence = importData(inputPath)
    cache = sequence[:4]
    count = 4
    
    for i in sequence[4:]:
        if testCache(cache):
            print(count)
            return 0

        count += 1
        cache = cache[1:] + i

    return 0

if __name__ == "__main__":
    main()
