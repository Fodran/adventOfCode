def importData():
    f = open("../input", "r")

    data = f.read()
    groupsAnswers = [x.split("\n") for x in data.split("\n\n")]
    groupsAnswers[-1].pop()
    
    f.close()
    
    return groupsAnswers



def countGroupYesQuestions(groupAnswers):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    count = {}

    for x in alphabet:
        count[x] = 0

    for personAnswers in groupAnswers:
        for letter in personAnswers:
            count[letter] += 1

    return sum(map(len(groupAnswers).__eq__, count.values()))



def sumAllYesQuestions(groupsAnswers):
    counter = 0

    for group in groupsAnswers:
        counter += countGroupYesQuestions(group)

    return counter



def main():
    print(sumAllYesQuestions(importData()))
    return 0



if __name__ == "__main__":
    main()
