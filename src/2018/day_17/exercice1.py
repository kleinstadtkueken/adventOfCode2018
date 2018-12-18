#!/usr/bin/python3

fileName = 'input.txt'
# fileName = 'testinput.txt'
# fileName = 'testinput2.txt'


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'(x={self.x}, y={self.y})'

def createGrid(inputs):
    global offsetX, spring
    minX = min(inputs, key=lambda e: e.x).x - 1
    maxX = max(inputs, key=lambda e: e.x).x + 1
    minY = 0
    maxY = max(inputs, key=lambda e: e.y).y
    offsetX = minX

    inputs.sort(key=lambda p: p.x)
    inputs.sort(key=lambda p: p.y)

    # Remove duplicates
    i = 0
    while i < len(inputs) - 1:
        if inputs[i].x == inputs[i+1].x and inputs[i].y == inputs[i+1].y:
            inputs.pop(i+1)
        else:
            i += 1

    currentIndex = 0

    for y in range(minY, maxY + 1):
        line = []
        for x in range(minX, maxX + 1):
            char = '.'
            if y == 0 and x == 500:
                char = '+'
            elif currentIndex < len(inputs) and inputs[currentIndex].x == x and inputs[currentIndex].y == y:
                char = '#'
                currentIndex += 1
            line.append(char)
        grid.append(line)


def printGrid():
    for line in grid:
        for char in line:
            print(char, end='')
        print()
    print()



def floatGrid(start: Point):
    currentBottom = fallDown(start)

    if currentBottom.x == start.x and currentBottom.y == start.y:
        return False


    if currentBottom.y + 1 == len(grid) or grid[currentBottom.y + 1][currentBottom.x] == '|':
        grid[currentBottom.y][currentBottom.x] = '|'
    else:
        if isBox(currentBottom):
            fillWithSettledWater(currentBottom)
        elif grid[currentBottom.y][currentBottom.x - 1] == '.':
            # fill left
            current = currentBottom
            while grid[current.y][current.x - 1] == '.':
                current = Point(current.x - 1, current.y)
                if grid[current.y + 1][current.x] == '.':
                    floatGrid(current)
                    break

                if grid[current.y + 1][current.x] == '|':
                    grid[current.y][current.x] = '|'
                    break

            if grid[current.y + 1][current.x] != '.' and grid[current.y][current.x - 1] in ['#', '|']:
                grid[current.y][current.x] = '|'

        elif grid[currentBottom.y][currentBottom.x + 1] == '.':
            # fill right
            current = currentBottom
            while grid[current.y][current.x + 1] == '.':
                current = Point(current.x + 1, current.y)
                if grid[current.y + 1][current.x] == '.':
                    floatGrid(current)
                    break

                if grid[current.y + 1][current.x] == '|':
                    grid[current.y][current.x] = '|'
                    break

            if grid[current.y + 1][current.x] != '.' and grid[current.y][current.x + 1] in ['#', '|']:
                grid[current.y][current.x] = '|'

        else:
            grid[currentBottom.y][currentBottom.x] = '|'

            # check if it's settled water
            current = currentBottom
            if grid[current.y + 1][current.x] not in ['#', '~']:
                return True

            while grid[current.y][current.x - 1] == '|' and grid[current.y + 1][current.x - 1] in ['#', '~']:
                current = Point(current.x - 1, current.y)

            if grid[current.y][current.x - 1] != '#':
                return True

            current = currentBottom
            while grid[current.y][current.x + 1] == '|' and grid[current.y + 1][current.x + 1] in ['#', '~']:
                current = Point(current.x + 1, current.y)

            if grid[current.y][current.x + 1] != '#':
                return True

            grid[current.y][current.x] = '~'
            while grid[current.y][current.x - 1] == '|':
                current = Point(current.x - 1, current.y)
                grid[current.y][current.x] = '~'


                # printGrid()
    return True


def fallDown(current: Point):
    while current.y + 1 < len(grid) and grid[current.y + 1][current.x] == '.':
        current = Point(current.x, current.y + 1)

    return current


def isBox(start: Point):

    current = start
    while grid[current.y][current.x - 1] == '.':
        current = Point(current.x -1 , current.y)
        if grid[current.y + 1][current.x] not in ['#', '~']:
            return False

    if grid[current.y][current.x - 1] != '#':
        return False

    current = start
    while grid[current.y][current.x + 1] == '.':
        current = Point(current.x + 1, current.y)
        if grid[current.y + 1][current.x] not in ['#', '~']:
            return False

    if grid[current.y][current.x + 1] != '#':
        return False

    return True


def fillWithSettledWater(current: Point):
    while grid[current.y][current.x - 1] == '.':
        current = Point(current.x - 1, current.y)

    grid[current.y][current.x] = '~'
    while grid[current.y][current.x + 1] == '.':
        current = Point(current.x + 1, current.y)
        grid[current.y][current.x] = '~'



grid = []
offsetX = 0

inputs = []

with open(fileName, 'r') as file:
    for line in file:
        xFirst = 'x' == line[0]
        elements = line[2:].split()
        elements[0] = elements[0][:-1]
        second = elements[1][2:].split('..')

        for i in range(int(second[0]), int(second[1]) + 1):
            if xFirst:
                inputs.append(Point(int(elements[0]), i))
            else:
                inputs.append(Point(i, int(elements[0])))
createGrid(inputs)


spring = Point(500 - offsetX, 0)
# printGrid()


going = True
while going:
    going = floatGrid(spring)




amountPipe = 0
amountTilde = 0


for y in range(min(inputs, key=lambda e: e.y).y, len(grid)):
    for x in range(0, len(grid[y])):
        if grid[y][x] == '|':
            amountPipe += 1
        if grid[y][x] == '~':
            amountTilde += 1

printGrid()

print(f'Total sum: {amountTilde + amountPipe}')
print(f'sum |: {amountPipe}')
print(f'sum ~: {amountTilde}')



# 886 Too Low
# 32073 Too High
# 32056 Too High
# 32053
# 31934 correct


















