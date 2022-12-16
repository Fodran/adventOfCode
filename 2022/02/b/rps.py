inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split('\n')[:-1]
        return data

#returns 0 for rock, 1 for paper, 2 for scissors
def chooseShape(opp, end):#opponent's choice and needed result
    #the same matrix is still usedd to find what our play should be
    shapes = {
            "A":0,
            "B":1,
            "C":2,
            "X":0,
            "Y":3,
            "Z":6
            }
    winMatrix = [[3, 6, 0],[0, 3, 6],[6, 0, 3]]
    play = winMatrix[shapes[opp]].index(shapes[end])
    print(play)
    return play

#returns score (shape + outcome)
def score(opp, end): #opponent's choice and our choice
    score = 0
    score += chooseShape(opp, end) + 1

    shapeScore = {
            "X":0,
            "Y":3,
            "Z":6
            }

    score += shapeScore[end]

    return score

def main():
    data = importData(inputPath)
    totalScore = 0
    line = 0

    for game in data:
        choices = game.split(" ")
        totalScore += score(choices[0], choices[1])
        line += 1
        print(choices, score(choices[0], choices[1]), totalScore)

    print(line)
    print(totalScore)
    return 0

if __name__ == "__main__":
    main()
