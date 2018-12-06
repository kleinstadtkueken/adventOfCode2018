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

theMap = [[0 for j in range(maxY)] for i in range(maxX)]


for p in range(len(input)):
    pX = input[p].x
    pY = input[p].y

    for i in range(len(theMap)):
        for j in range(len(theMap[i])):
            distance = abs(i - pX) + abs(j - pY)

            theMap[i][j] += distance


result = 0
for i in range(len(theMap)):
    for j in range(len(theMap[i])):
        if theMap[i][j] < 10000:
            result += 1

print(result)
