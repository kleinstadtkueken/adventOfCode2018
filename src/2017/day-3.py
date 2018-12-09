#!/usr/bin/python3

def move(position, change):
    return position[0] + change[0], position[1] + change[1]

def foo(neededSteps, pos, change):

    for _ in range(neededSteps):
        pos = move(pos, change)
        sum = 0
        for x in range(pos[0] - 1, pos[0] + 2):
            for y in range(pos[1] - 1, pos[1] + 2):
                sum += grid[x][y]


        if sum > input:
            print(sum)
            return None

        grid[pos[0]][pos[1]] = sum

    return pos


input = 368078

# find grid width
gridWidth = 1

while gridWidth * gridWidth <= input:
    gridWidth += 2

maxElement = gridWidth * gridWidth

# "real" steps of input from down right corner
stepsFromLowerRight = maxElement - input

# element is in the lowest row
neededSteps = (stepsFromLowerRight - (607 // 2)) + (607 // 2)

print(neededSteps)


grid = [[0 for j in range(201)] for i in range(201)]
position = 100, 100

grid[position[0]][position[1]] = 1

stepsInOneDirection = 0

while True:
    # right
    stepsInOneDirection +=1
    position = foo(stepsInOneDirection, position, (1, 0))
    if position is None:
        break

    # up
    position = foo(stepsInOneDirection, position, (0, -1))
    if position is None:
        break

    # left
    stepsInOneDirection +=1
    position = foo(stepsInOneDirection, position, (-1, 0))
    if position is None:
        break

    # down
    position = foo(stepsInOneDirection, position, (0, 1))
    if position is None:
        break


print("done")
