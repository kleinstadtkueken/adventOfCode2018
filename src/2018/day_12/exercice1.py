#!/usr/bin/python3

currentState = '#..####.##..#.##.#..#.....##..#.###.#..###....##.##.#.#....#.##.####.#..##.###.#.......#............'
# desiredGenerations = 12
desiredGenerations = 50000000000

notes = dict()

with open('input.txt', 'r') as file:
    for line in file:
        content = line.split()
        notes[content[0]] = content[2]

potsAdded = 0
previousSum = 0
previousDifference = 0
generation = 0
sumOfPotNumbers = 0


while generation < desiredGenerations:
    generation += 1

    if currentState[0:5] != '.....':
        potsAdded +=2
        currentState = '..' + currentState
    if currentState[-5:] != '.....':
        currentState += '.....'

    nextState = '..'
    for i in range(2, len(currentState) - 2):
        nextState += notes[currentState[ i-2 : i+3 ]]

    currentState = nextState

    sumOfPotNumbers = 0
    for i in range(len(currentState)):
        if currentState[i] == '#':
            sumOfPotNumbers += i - potsAdded

    print(currentState, sumOfPotNumbers, sumOfPotNumbers - previousSum)

    if previousDifference == sumOfPotNumbers - previousSum:
        break

    previousDifference = sumOfPotNumbers - previousSum
    previousSum = sumOfPotNumbers

sumOfPotNumbers += (desiredGenerations - generation) * previousDifference


print(generation, sumOfPotNumbers)
