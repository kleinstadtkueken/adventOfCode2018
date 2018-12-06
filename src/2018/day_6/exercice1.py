#!/usr/bin/python3
import operator


class Info:
    def __init__(self):
        self.minDistance = None
        self.pointId = None


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y


input = []

with open('input.txt', 'r') as file:
    for line in file:
        c = line.split(',')
        coordinate = Coordinate(int(c[0]), int(c[1]))

        input.append(coordinate)

input.sort(key=lambda c: c.x, reverse=True)
maxX = input[0].x
input.sort(key=lambda c: c.y, reverse=True)
maxY = input[0].y

theMap = [[Info() for j in range(maxY)] for i in range(maxX)]


for p in range(len(input)):
    pX = input[p].x
    pY = input[p].y

    for i in range(len(theMap)):
        for j in range(len(theMap[i])):
            distance = abs(i - pX) + abs(j - pY)

            if theMap[i][j].minDistance is None or distance < theMap[i][j].minDistance:
                theMap[i][j].minDistance = distance
                theMap[i][j].pointId = p
            elif distance == theMap[i][j].minDistance:
                theMap[i][j].minDistance = -1
                theMap[i][j].pointId = None


borderElements = set()

for i in range(maxX):
    borderElements.add(theMap[i][0].pointId)
    borderElements.add(theMap[i][maxY - 1].pointId)

for j in range(maxY):
    borderElements.add(theMap[0][j].pointId)
    borderElements.add(theMap[maxX - 1][j].pointId)

results = dict()
for i in range(len(theMap)):
    for j in range(len(theMap[i])):
        if theMap[i][j].pointId not in borderElements:
            if theMap[i][j].pointId not in results:
                results[theMap[i][j].pointId] = 0

            results[theMap[i][j].pointId] += 1

print(max(results.items(), key=operator.itemgetter(1))[1])
