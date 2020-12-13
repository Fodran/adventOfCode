path = "../input"
startPosition = [0, 0, "E"]


def importData(path):
    f = open(path, "r")
    
    data = [line for line in f]

    f.close()

    return data



def move(position, instruction):
    south = position[0]
    east = position[1]
    orientation = position[2]
    command = instruction[0]
    value = int(instruction[1:])

    if(command == "F"):
        command = orientation

    if(command == "N"):
        south -= value
    elif(command == "S"):
        south += value
    elif(command == "E"):
        east += value
    elif(command == "W"):
        east -= value
    else:
        orientation = rotate(orientation, command, value)
    print(south, east, orientation)
    return [south, east, orientation]



def rotate(orientation, command, value):
    directions = ["E", "S", "W", "N"]

    stops = (value / 90) % 4
    index = directions.index(orientation)

    if(command == "R"):
        index = (index + stops) % 4
    else:
        index = (index - stops) % 4

    return directions[int(index)]



def navigate(directions):
    position = startPosition[:]

    for instruction in directions:
        position = move(position, instruction)

    return position



def manhattanDistance(position):
    return abs(position[0]) + abs(position[1])



def main():
    directions = importData(path)
    finalPosition = navigate(directions)
    print(manhattanDistance(finalPosition))

    return 0



if __name__ == "__main__":
    main()
