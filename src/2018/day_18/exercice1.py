#!/usr/bin/python3

fileName = 'input.txt'
# fileName = 'testinput.txt'

def printGrid(theGrid):
    [print(''.join(line)) for line in grid]
    print()


def countSurrounding(currentX, currentY):
    open = tree = lumber = 0

    for x in range(currentX - 1, currentX + 2):
        for y in range(currentY - 1, currentY + 2):
            if 0 <= x < len(grid[0]) and 0 <= y < len(grid) and not (x == currentX and y == currentY):
                if grid[y][x] == '.':
                    open += 1
                elif grid[y][x] == '|':
                    tree += 1
                else:
                    lumber += 1

    return open, tree, lumber



def doStep():
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            open, tree, lumber = countSurrounding(x, y)

            if char == '.':
                if tree >= 3:
                    next[y][x] = '|'
                else:
                    next[y][x] = '.'

            if char == '|':
                if lumber >= 3:
                    next[y][x] = '#'
                else:
                    next[y][x] = '|'

            if char == '#':
                if lumber > 0 and tree > 0:
                    next[y][x] = '#'
                else:
                    next[y][x] = '.'

    return next, grid


grid = []

with open(fileName, 'r') as file:
    for inputLine in file:
        line = []
        for char in inputLine[:-1]:
            line.append(char)
        grid.append(line)

next = [['.' for x in range(len(grid[0]))] for y in range(len(grid))]

printGrid(grid)

seen = {}
totalCycles = 1000000000

for i in range(1, 10000):
    grid, next = doStep()

    gridstr = ''.join([''.join(line) for line in grid])

    if gridstr in seen:
        printGrid(grid)
        cycleLength = i - seen[gridstr]
        cyclesLeft = totalCycles - i
        print(f'currentStep: {i}\t lastStep: {seen[gridstr]} \t cycleLength: {cycleLength}')

        for j in range(cyclesLeft % cycleLength):
            grid, next = doStep()

        break
    else:
        seen[gridstr] = i


    tree = lumber = 0
    for line in grid:
        for char in line:
            if char == '|':
                tree += 1
            if char == '#':
                lumber += 1

    # printGrid(grid)
    # print()


tree = lumber = 0
for line in grid:
    for char in line:
        if char == '|':
            tree += 1
        if char == '#':
            lumber += 1

printGrid(grid)
print(tree * lumber)
