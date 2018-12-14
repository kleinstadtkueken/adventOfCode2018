#!/usr/bin/python3

from enum import Enum, auto


class Turn(Enum):
    LEFT = auto()
    RIGHT = auto()
    STRAIGT = auto()

    # def next(self):
    #     if self.LEFT:
    #         return self.STRAIGT
    #     elif self.STRAIGT:
    #         return self.RIGHT
    #     elif self.RIGHT:
    #         return self.LEFT
    #     else:
    #         raise Exception('Falscher Turn')


class Direction(Enum):
    UP = ('^')
    DOWN = ('v')
    RIGHT = ('>')
    LEFT = ('<')

    def __init__(self, symbol):
        self.symbol = symbol

    def move(self, currentPosition):
        if self == self.UP:
            return currentPosition[0], currentPosition[1] - 1
        elif self == self.DOWN:
            return currentPosition[0], currentPosition[1] + 1
        elif self == self.RIGHT:
            return currentPosition[0] + 1, currentPosition[1]
        elif self == self.LEFT:
            return currentPosition[0] - 1, currentPosition[1]

    def turnLeft(self):
        if self == self.UP:
            return self.LEFT

        elif self == self.DOWN:
            return self.RIGHT

        elif self == self.RIGHT:
            return self.UP

        elif self == self.LEFT:
            return self.DOWN

    def turnRight(self):
        if self == self.UP:
            return self.RIGHT

        elif self == self.DOWN:
            return self.LEFT

        elif self == self.RIGHT:
            return self.DOWN

        elif self == self.LEFT:
            return self.UP


    def nextDirection(self, track, nextTurn: Turn):
        if track == '-' or track == '|':
            return self, nextTurn

        elif track == '/':
            if self == self.UP:
                return self.RIGHT, nextTurn
            elif self == self.DOWN:
                return self.LEFT, nextTurn
            elif self == self.LEFT:
                return self.DOWN, nextTurn
            elif self == self.RIGHT:
                return self.UP, nextTurn

        elif track == '\\':
            if self == self.UP:
                return self.LEFT, nextTurn
            elif self == self.DOWN:
                return self.RIGHT, nextTurn
            elif self == self.LEFT:
                return self.UP, nextTurn
            elif self == self.RIGHT:
                return self.DOWN, nextTurn

        elif track == '+':
            if nextTurn == Turn.STRAIGT:
                return self, Turn.RIGHT
            elif nextTurn == Turn.LEFT:
                return self.turnLeft(), Turn.STRAIGT
            elif nextTurn == Turn.RIGHT:
                return self.turnRight(), Turn.LEFT
        else:
            raise Exception('cart is of the track')



class Cart:
    def __init__(self, position, direction: Direction):
        self.position = position
        self.direction = direction
        self.nextTurn = Turn.LEFT

    # def __cmp__(self, other):
    #     if self.position[0] < other.position[0]:
    #         return -1
    #     elif self.position[0] > other.position[0]:
    #         return 1
    #     # the x coordinates are identical. Now the y coordinate is checked
    #     elif self.position[1] < other.position[1]:
    #         return -1
    #     elif self.position[1] > other.position[1]:
    #         return 1
    #     else:
    #         return 0
    #
    # def __lt__(self, other):
    #     if self.__cmp__(other) <= 1:
    #         return True
    #     else:
    #         return False


    def move(self):
        p = self.position
        self.position = self.direction.move(self.position)

        # print(f'Previous {p} {self.direction} current {self.position}')

        self.direction, self.nextTurn = self.direction.nextDirection(grid[self.position[1]][self.position[0]], self.nextTurn)





grid = []
carts = []

# with open('testInput.txt', 'r') as file:
with open('input.txt', 'r') as file:
    for y, line in enumerate(file):
        line = line[:-1]
        changes = dict()

        for x, char in enumerate(line):
            if char == '>':
                carts.append(Cart((x, y), Direction.RIGHT))
                changes[x] = '-'
            if char == '<':
                carts.append(Cart((x, y), Direction.LEFT))
                changes[x] = '-'
            if char == '^':
                carts.append(Cart((x, y), Direction.UP))
                changes[x] = '|'
            if char == 'v':
                carts.append(Cart((x, y), Direction.DOWN))
                changes[x] = '|'

        for x, change in changes.items():
            line = line[:x] + change + line[x+1:]

        grid.append(line)


def pickNewRecipe(position):
    steps = scoreBoard[position] + 1
    position += 1 + steps

    if len(scoreBoard) <= position:
        position %= len(scoreBoard)

    return position


# inputRounds = 503761
inputRounds = 9

scoreBoard = [3, 7]

firstElve = 0
secondElve = 1

currentRound = 0

for _ in range(inputRounds + 10):
    createNewRecipe()
    pickNewRecipe()

print(scoreBoard)


