#!/usr/bin/python3

def printCave():
    units.sort(key=lambda u: u.x)
    units.sort(key=lambda u: u.y)
    for y, line in enumerate(cave):
        for char in line:
            print(char, end='')
        print('   ', end='')
        for u in units:
            if u.y == y:
                print(u, end=' ')

        print()


def getDistances(startPoints):
    nextPoints = []
    distanceMap = [[1000 for x in range(len(cave[0]))] for y in range(len(cave))]

    for point in startPoints:
        distanceMap[point.y][point.x] = 0
        nextPoints.append(point)

    while len(nextPoints) > 0:
        point = nextPoints.pop(0)
        x = point.x
        y = point.y
        nextDistance = distanceMap[y][x] + 1

        if y > 0 and cave[y-1][x] == '.' and nextDistance < distanceMap[y-1][x]:
            distanceMap[y-1][x] = nextDistance
            nextPoints.append(Point(x, y-1))

        if y + 1 < len(distanceMap) and cave[y+1][x] == '.' and nextDistance < distanceMap[y+1][x]:
            distanceMap[y+1][x] = nextDistance
            nextPoints.append(Point(x, y+1))


        if x > 0 and cave[y][x-1] == '.' and nextDistance < distanceMap[y][x-1]:
            distanceMap[y][x-1] = nextDistance
            nextPoints.append(Point(x-1, y))

        if x + 1 < len(distanceMap) and cave[y][x+1] == '.' and nextDistance < distanceMap[y][x+1]:
            distanceMap[y][x+1] = nextDistance
            nextPoints.append(Point(x+1, y))

    return distanceMap


class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'({self.x},{self.y})'
    def __str__(self):
        return f'({self.x},{self.y})'


class Unit:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.attackPower = 3
        self.hitPoints = 200

    def __str__(self):
        return f'{self.type}({self.hitPoints})'

    def __repr__(self):
        return f'{self.type} at ({self.x}, {self.y}) -- {self.hitPoints}'

    def getTargets(self):
        targets = []
        for unit in units:
            if self.type != unit.type:
                targets.append(unit)
        return targets

    def getAvailableSpotsNextToSelf(self):
        availableSpots = []
        if self.x > 0 and cave[self.y][self.x-1] == '.': availableSpots.append(Point(self.x-1, self.y))
        if self.x + 1 < len(cave[self.y]) and cave[self.y][self.x+1] == '.': availableSpots.append(Point(self.x+1, self.y))
        if self.y > 0 and cave[self.y-1][self.x] == '.': availableSpots.append(Point(self.x, self.y-1))
        if self.y + 1 < len(cave) and cave[self.y+1][self.x] == '.': availableSpots.append(Point(self.x, self.y+1))
        return availableSpots

    def isInReach(self, target):
        if (abs(self.x - target.x) == 1 and abs(self.y - target.y) == 0) or (abs(self.x - target.x) == 0 and abs(self.y - target.y) == 1):
            return True
        else:
            return False

    def move(self):
        destinations = []
        for target in self.getTargets():
            if self.isInReach(target):
                return
            destinations.extend(target.getAvailableSpotsNextToSelf())

        distanceMap = getDistances(destinations)

        options = [
            distanceMap[self.y-1][self.x],
            distanceMap[self.y][self.x-1],
            distanceMap[self.y][self.x+1],
            distanceMap[self.y+1][self.x],
        ]
        minDistance = min(options)
        if minDistance < 1000:

            if options[0] == minDistance:
                nextPoint = Point(self.x, self.y-1)
            elif options[1] == minDistance:
                nextPoint = Point(self.x-1, self.y)
            elif options[2] == minDistance:
                nextPoint = Point(self.x+1, self.y)
            elif options[3] == minDistance:
                nextPoint = Point(self.x, self.y+1)

            cave[self.y][self.x] = '.'
            cave[nextPoint.y][nextPoint.x] = self.type
            self.x = nextPoint.x
            self.y = nextPoint.y

    def attack(self):
        # get opponent
        targets = []
        for target in self.getTargets():
            if self.isInReach(target):
                targets.append(target)

        if len(targets) == 0:
            return
        elif len(targets) == 1:
            opponent = targets[0]
        else:
            minHitPoints = min(targets, key=lambda u: u.hitPoints)
            minHitpointsOpponents = []
            for target in targets:
                if target.hitPoints == minHitPoints.hitPoints:
                    minHitpointsOpponents.append(target)

            if len(minHitpointsOpponents) > 1:
                minHitpointsOpponents.sort(key=lambda t: t.x)
                minHitpointsOpponents.sort(key=lambda t: t.y)
            opponent = minHitpointsOpponents[0]

        # do attack
        opponent.hitPoints -= self.attackPower

        if opponent.hitPoints <= 0:
            cave[opponent.y][opponent.x] = '.'
            units.remove(opponent)





currentRound = 0
cave = []
units = []

with open('input.txt', 'r') as file:
# with open('testInput3.txt', 'r') as file:
    for y, inputLine in enumerate(file):
        line = []
        for x, char in enumerate(inputLine):
            if char != '\n':
                line.append(char)

            if char == 'E' or char == 'G':
                units.append(Unit(char, x, y))
        cave.append(line)



while True:

    # print()
    # print(currentRound)
    # printCave()

    units.sort(key=lambda u: u.x)
    units.sort(key=lambda u: u.y)

    previousUnits = list(units)

    for index, unit in enumerate(previousUnits):
        if unit.hitPoints > 0:
            unit.move()
            unit.attack()

        if index + 1 == len(previousUnits) and len(units[0].getTargets()) != 0:
            currentRound += 1

    if len(units[0].getTargets()) == 0:
        break


print()
print('End')
printCave()

totalHitpoints = sum(u.hitPoints for u in units)

print(f'\n\n{currentRound} * {totalHitpoints} = {totalHitpoints * currentRound}')
# print(f'\n\n{currentRound - 1} * {totalHitpoints} = {totalHitpoints * (currentRound-1)}')



# no more targets --> combat ends

# identify targets
# find open squares in reach of each target

# if in reach of a target --> no move
# if no open squares --> no move & no combat






