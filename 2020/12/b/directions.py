path = "../input"
# Position is x, y and facing direction
startPosition = [0, 0]
# Waypoint is x and y (not y and x as presented in the puzzle)
startWaypoint = [-1, 10]



def importData(path):
    f = open(path, "r")
    
    data = [line for line in f]

    f.close()

    return data



def move(position, waypoint, instruction):
    southP = position[0]
    eastP = position[1]
    southW = waypoint[0]
    eastW = waypoint[1]
    command = instruction[0]
    value = int(instruction[1:])

    if(command == "F"):
        southP += southW * value
        eastP += eastW * value
    elif(command == "N"):
        southW -= value
    elif(command == "S"):
        southW += value
    elif(command == "E"):
        eastW += value
    elif(command == "W"):
        eastW -= value
    else:
        southW, eastW = rotate(waypoint, command, value)
    print("position = " + str(southP) + "; " + str(eastP) + "\nwaypoint = " + str(southW) + "; " + str(eastW) + "\n")
    return [southP, eastP], [southW, eastW]



def plus90(waypoint):
    return waypoint[1], -waypoint[0]



def minus90(waypoint):
    return -waypoint[1], waypoint[0]



def r180(waypoint):
    return -waypoint[0], -waypoint[1]



def rotate(waypoint, command, value):
    if(value == 180):
        return r180(waypoint)

    if(command == "L"):
        value = (value + 180) % 360

    if(value == 90):
        return plus90(waypoint)
    else:
        return minus90(waypoint)



def navigate(directions):
    position = startPosition[:]
    waypoint = startWaypoint[:]

    for instruction in directions:
        position, waypoint = move(position, waypoint, instruction)

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
