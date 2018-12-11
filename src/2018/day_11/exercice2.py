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
sizeOfMaxPower = 1
point = None

for currentSize in range(1, gridSize + 1):
    for x in range(1, gridSize + 1 - currentSize):
        for y in range(1, gridSize + 1 - currentSize):
            currentPower = 0
            for i in range(currentSize):
                for j in range(currentSize):
                    currentPower += grid[x + i][y + j]

            if currentPower > maxPower:
                maxPower = currentPower
                point = (x, y)
                sizeOfMaxPower = currentSize

    print(f'currentent Size {currentSize}: Power: {maxPower}, {point},{sizeOfMaxPower}')

print(f'max power: {maxPower} at {point},{sizeOfMaxPower}')
