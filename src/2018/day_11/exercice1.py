#!/usr/bin/python3


serialNumber = 5153
gridSize = 300

grid = [[None for j in range(gridSize + 1)] for i in range(gridSize + 1)]

for x in range(1, gridSize + 1):
    for y in range(1, gridSize + 1):
        rackId = (x + 10)
        powerLevel = (((((rackId * y) + serialNumber) * rackId) // 100) % 10) - 5
        grid[x][y] = powerLevel

maxPower = 0
point = None

for x in range(1, gridSize - 2):
    for y in range(1, gridSize - 2):
        currentPower = 0
        for i in range(3):
            for j in range(3):
                currentPower += grid[x + i][y + j]

        if currentPower > maxPower:
            maxPower = currentPower
            point = (x, y)

print(maxPower, point)
