inputPath = "../input"

def importData(filePath):
    with open(filePath) as file:
        data = file.read().split('\n')[:-1]
        return data

#returns 0 if lost, 3 if tie, 6 if we win
def outcome(opp, us):#opponent's choise and our choice
    #we'll use a win matrix, row being opp's choice, col being our to check who wins
    #this simplifies the check (instead of using huge amounts of ifs)
    shapes = {
            "A":0,
            "B":1,
            "C":2,
            "X":0,
            "Y":1,
            "Z":2
            }
    winMatrix = [[3, 6, 0],[0, 3, 6],[6, 0, 3]]
    outcome = winMatrix[shapes[opp]][shapes[us]]
    return outcome

#returns score (shape + outcome)
def score(opp, us): #opponent's choice and our choice
    score = 0
    score += outcome(opp, us)

    shapeScore = {
            "X":1,
            "Y":2,
            "Z":3
            }

    score += shapeScore[us]

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
