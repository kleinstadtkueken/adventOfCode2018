#!/usr/bin/python3


class Point:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def moveOneStep(self):
        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def moveOneStepBack(self):
        self.position[0] -= self.velocity[0]
        self.position[1] -= self.velocity[1]


def findExtremes(points):
    minPoint = (min(points, key=lambda p: p.position[0]).position[0], min(points, key=lambda p: p.position[1]).position[1])
    maxPoint = (max(points, key=lambda p: p.position[0]).position[0], max(points, key=lambda p: p.position[1]).position[1])
    return minPoint, maxPoint

def getSize(points):
    minPoint, maxPoint = findExtremes(points)
    width = maxPoint[0] - minPoint[0]
    height = maxPoint[1] - minPoint[1]

    return width * height


def printGrid(points):
    minPoint, maxPoint = findExtremes(points)

    grid = [['.' for x in range(minPoint[0], maxPoint[0] + 1)] for y in range(minPoint[1], maxPoint[1] + 1)]

    for point in points:
        grid[point.position[1] - minPoint[1]][point.position[0] - minPoint[0]] = '#'

    for line in grid:
        print(''.join(line))


points = []


with open('input.txt', 'r') as file:
    for line in file:
        inputs = line.split('<')
        p = inputs[1].split('>')[0].split(',')
        v = inputs[2].split('>')[0].split(',')
        points.append(Point([int(p[0]), int(p[1])], [int(v[0]), int(v[1])]))


lastSize = getSize(points)
i = 0

print(f'{i} sec: {lastSize} ')

while True:
    for p in points:
        p.moveOneStep()
    currentSize = getSize(points)

    if currentSize > lastSize:
        break

    lastSize = currentSize
    i += 1
    print(f'{i} sec: {lastSize} ')


for p in points:
    p.moveOneStepBack()
printGrid(points)


