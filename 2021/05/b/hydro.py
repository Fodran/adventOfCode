import numpy as np

inputPath = "../input"

def importData(pathToFile):
    with open(pathToFile) as file:
        data = file.read()
    lines = data.split('\n')[:-1]
    return lines

def digestData(data):
    digest = list(map(lambda x: x.split('->'), data))
    digest = [list(map(lambda x: x.split(','), i)) for i in digest]
    digest = [list(map(lambda x: [int(x[0]), int(x[1])], i)) for i in digest]
    return digest

def isSegmentValid(segment):
    pointA = segment[0]
    pointB = segment[1]
    if pointA[0] == pointB[0] or pointA[1] == pointB[1]:
        return True
    return False

def selectValidSegments(segments):
    validSegments = []
    for s in segments:
        if isSegmentValid(s):
            validSegments.append(s)
    return validSegments

def extendSegment(segment):
    points = []
    step = 1
    pointA = segment[0]
    pointB = segment[1]
    if pointA[0] == pointB[0]:
        if pointB[1] < pointA[1]:
            step = -1
        for i in range(pointA[1], pointB[1] + step, step):
            points.append([pointA[0], i])
    else:
        if pointB[0] < pointA[0]:
            step = -1
        for i in range(pointA[0], pointB[0] + step, step):
            points.append([i, pointA[1]])
    return points


def applySegments(segments):
    values = {}
    for s in segments:
        points = extendSegment(s)
        for p in points:
            values[tuple(p)] = values.get(tuple(p), 0) + 1
    return values

def countPoints(values_dict):
    counter = 0
    for value in values_dict.values():
        if value > 1:
            counter += 1
    return counter

def main():
    data = digestData(importData(inputPath))
    segments = selectValidSegments(data)
    print(countPoints(applySegments(segments)))
    return 0

if __name__ == "__main__":
    main()
