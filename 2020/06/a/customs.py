def importData():
    f = open("../input", "r")

    data = f.read()
    groupsAnswers = [x.replace("\n", "") for x in data.split("\n\n")]
    
    f.close()
    
    return groupsAnswers



def countGroupYesQuestions(groupAnswers):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    count = {}

    for x in alphabet:
        count[x] = 0

    for letter in groupAnswers:
        count[letter] = 1

    return sum(map((1).__eq__, count.values()))



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
