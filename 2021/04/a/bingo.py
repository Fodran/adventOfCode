inputPath = "../input"

def importData(pathToFile):
    lines = []
    with open(pathToFile) as file:
        data = file.read()[:-1].replace('  ', ' ').replace("\n ", '\n')
    return data

def digestData(data):
    digest = data.split("\n\n")
    numbers = digest[0].split(",")
    numbers = [int(i) for i in numbers]
    tables = []
    # at this point digest is composed of tables in the form of strings
    for tmpTable in digest[1:]:
        # tableStrings takes the form of strings that are its lines
        tableStrings = tmpTable.split("\n")
        table = []
        # now we want to replace string lines by lists of INTs
        for tmpLine in tableStrings:
            # tmpLine is a string line
            # Line becomes a list of numbers but in str
            line = tmpLine.split(' ')
            # then we cast line into itself to make it out of int
            line = [int(i) for i in line]
            # at this point line is a list of ints
            # and we want to append it to the table
            table.append(line)
        tables.append(table)
    return tables, numbers

# Calculate how many turns it takes the given table to win
def turnsToWin(table, numbers):
    for i in range(len(numbers)):
        if isWin(table, numbers[:i + 1]):
            return i
    return len(numbers)

# Test if the table wins with given numbers
def isWin(table, numbers):
    # Check lines for win
    for line in table:
        win = True
        for number in line:
            if number not in numbers:
                win = False
                break
        if win:
            return win
    # Check columns for win
    for i in range(len(table[0])):
        win = True
        for line in table:
            if line[i] not in numbers:
                win = False
                break
        if win:
            return win
    return win

# Calculate the score with given marked numbers
def calcScore(table, numbers):
    score = 0
    for line in table:
        for num in line:
            if num not in numbers:
                score += num
    score = score * numbers[-1]
    return score

# Find winning table
def winningTable(tables, numbers):
    minTurns = len(numbers)
    minTable = tables[0].copy()
    for table in tables:
        turns = turnsToWin(table, numbers)
        if turns < minTurns:
            minTurns = turns
            minTable = table.copy()
    print(calcScore(minTable, numbers[:minTurns + 1]))
    return 0

def main():
    tables, numbers = digestData(importData(inputPath))
    winningTable(tables, numbers)
    return 0

if __name__ == "__main__":
    main()
