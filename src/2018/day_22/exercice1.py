#!/usr/bin/python3

from collections import namedtuple
from enum import Enum


Point = namedtuple('Point', ['x', 'y'])

class Gear(Enum):
    NEITHER = 0
    TORCH = 1
    CLIMBING = 2


class Type(Enum):
    ROCKY  = (0, '.', {Gear.CLIMBING, Gear.TORCH})
    WET    = (1, '=', {Gear.CLIMBING, Gear.NEITHER})
    NARROW = (2, '|', {Gear.TORCH, Gear.NEITHER})

    def __init__(self, riskLevel, typeStr, allowedGear):
        self.riskLevel = riskLevel
        self.typeStr = typeStr
        self.allowedGear = allowedGear

    @staticmethod
    def getForErosionLevel(level):
        erosionLevel = level % 3
        if erosionLevel == 0:
            return Type.ROCKY
        elif erosionLevel == 1:
            return Type.WET
        else:
            return Type.NARROW


depth = 8787
target = Point(10, 725)
# depth = 510
# target = Point(10, 10)

maxX = target.x + 100
maxY = target.y + 100

cave = [[None for _ in range(maxX)] for _ in range(maxY)]
erosionLevels = [[None for _ in range(maxX)] for _ in range(maxY)]

totalRiskLevel = 0

for y in range(maxY):
    for x in range(maxX):

        if (x == 0 and y == 0) or (x == target.x and y == target.y):
            geologicIndex = 0
        elif y == 0:
            geologicIndex = x * 16807
        elif x == 0:
            geologicIndex = y * 48271
        else:
            geologicIndex = erosionLevels[y-1][x] * erosionLevels[y][x-1]

        erosionLevels[y][x] = (geologicIndex + depth) % 20183

        cave[y][x] = Type.getForErosionLevel(erosionLevels[y][x])

        if x <= target.x and y <= target.y:
            totalRiskLevel += cave[y][x].riskLevel

print(f'Total risk level for part 1: {totalRiskLevel}')


def calculateOther(p: Point, currentGear: Gear):

    for gear in Gear:
        if gear in cave[p.y][p.x].allowedGear and gear != currentGear and \
                (durationMap[p.y][p.x][gear] is None or
                 durationMap[p.y][p.x][gear] > durationMap[p.y][p.x][currentGear] + changingDuration):

            durationMap[p.y][p.x][gear] = durationMap[p.y][p.x][currentGear] + changingDuration


def move(current, next):
    valueChanged = False
    allowedGear = cave[current.y][current.x].allowedGear & cave[next.y][next.x].allowedGear

    for gear in allowedGear:
        if durationMap[next.y][next.x][gear] is None or \
            durationMap[next.y][next.x][gear] > durationMap[current.y][current.x][gear] + moveDuration:

            valueChanged = True
            durationMap[next.y][next.x][gear] = durationMap[current.y][current.x][gear] + moveDuration

    if len(allowedGear) == 1 and valueChanged:
        calculateOther(next, allowedGear.pop())

    if valueChanged:
        pointsToVisit.append(next)



moveDuration = 1
changingDuration = 7

durationMap = [[{Gear.TORCH:None, Gear.CLIMBING:None, Gear.NEITHER:None} for _ in range(maxX)] for _ in range(maxY)]

durationMap[0][0][Gear.TORCH] = 0
calculateOther(Point(0, 0), Gear.TORCH)

pointsToVisit = [Point(0, 0)]


while len(pointsToVisit) > 0:
    currentPoint = pointsToVisit.pop(0)

    # up
    if currentPoint.y > 0:
        next = Point(currentPoint.x, currentPoint.y - 1)
        move(currentPoint, next)

    # left
    if currentPoint.x > 0:
        next = Point(currentPoint.x - 1, currentPoint.y)
        move(currentPoint, next)

    # right
    if currentPoint.y + 1 < maxY:
        next = Point(currentPoint.x, currentPoint.y + 1)
        move(currentPoint, next)

    # down
    if currentPoint.x + 1 < maxX:
        next = Point(currentPoint.x + 1, currentPoint.y)
        move(currentPoint, next)


print(durationMap[target.y][target.x])






