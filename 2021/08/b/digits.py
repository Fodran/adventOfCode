inputPath = "../input2"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
numberDict = {1: 'cf', 2: 'acdeg', 3: 'acdfg', 4: 'bcdf', 5: 'abdfg', 6: 'abdefg', 7: 'acf', 8: 'abcdefg', 9: 'abcdfg', 0: 'abcefg'}
numDict = {}
segDict = {}

def importData(pathToFile):
    with open(pathToFile) as file:
        data = [i.split(' ') for i in file.read().split('\n')][:-1]
        data = [list(map(orderCode, i)) for i in data] 
    return data

def inAinB(isIn1, code1, isIn2, code2, isIn3, dict1):
    for l in letters:
        if l in code1 == isIn1 and l in code2 == isIn2 and l in dict1 == isIn3:
                return l

def decodeNum(code):
    return list(knownDict.keys())[list(knownDict.values()).index(code)]
        
def decodeLine(line):
    num = ''
    for code in line:
        num += decodeNum(code)
    return int(num)

def orderCode(code):
    return ''.join(sorted(code))

def decipher(line):
    global numDict
    global segDict
    numDict = {}
    segDict = {}
    for l in line:
        if len(l) == 2:
            knownDict[1] = l
        elif len(l) == 3:
            knownDict[7] = l
        elif len(l) == 4:
            knownDict[4] = l
        elif len(l) == 7:
            knownDict[8] = l
    segDict[inAinB(False, numDict[1], True, numDict[7])] = 'a'
    segDict[inAinB(True, numDict[1], False, numDict[5])] = 'c'
    segDict[inAinB(True, numDict[1], True, numDict[5])] = 'f'
    segDict[inAinB(False, numDict[1], True, numDict[7])] = 'a'
    segDict[inAinB(False, numDict[1], True, numDict[7])] = 'a'
    segDict[inAinB(False, numDict[1], True, numDict[7])] = 'a'
    segDict[inAinB(False, numDict[1], True, numDict[7])] = 'a'
    return numDict

def main():
    data = importData(inputPath)
    print(data)
    count = 0
    global knownDict
    for line in data:
        knownDict = decipher(line[:10])
        count += decodeLine(line[-4:])
    return 0

if __name__ == "__main__":
    main()
