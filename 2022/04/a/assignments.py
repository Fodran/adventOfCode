inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split('\n')[:-1]
        return data

def contained(duo):
    d1, d2 = [a.split('-') for a in duo.split(',')]
    d1 = [int(i) for i in d1]
    d2 = [int(i) for i in d2]
    
    if(d1[0] <= d2[0] and d1[1] >= d2[1] or d1[0] >= d2[0] and d1[1] <= d2[1]):
        return True

    return False

def main():
    duos = importData(inputPath)
    count = 0

    for duo in duos:
        if(contained(duo)):
            count += 1

    print(count)
    return 0

if __name__ == "__main__":
    main()
