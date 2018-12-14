#!/usr/bin/python3

def createNewRecipe():
    newScore = scoreBoard[firstElve] + scoreBoard[secondElve]

    if newScore > 20:
        raise Exception('should not happen')
    if newScore >= 10:
        scoreBoard.append(1)
        newScore -= 10
    scoreBoard.append(newScore)


def pickNewRecipe(position):
    steps = scoreBoard[position] + 1
    position += steps

    if len(scoreBoard) <= position:
        position %= len(scoreBoard)

    return position


def printBoard():
    for i, score in enumerate(scoreBoard):
        if firstElve == i:
            print(f'({score})', end='')
        elif secondElve == i:
            print(f'[{score}]', end='')
        else:
            print(f' {score} ', end='')
    print()


input = 503761
# input = 990941
# input = 2018
# input = 51589

scoreBoard = [3, 7]

firstElve = 0
secondElve = 1


def part1():
    global firstElve, secondElve

    while len(scoreBoard) < input + 10:
        createNewRecipe()
        firstElve = pickNewRecipe(firstElve)
        secondElve = pickNewRecipe(secondElve)
        # printBoard()

    print(''.join(map(str, scoreBoard[input:input + 10])))


def part2():
    global firstElve, secondElve, input
    lastCheckedStartIndex = 0
    inputLength = len(str(input))
    input = str(input)

    while True:
        createNewRecipe()
        firstElve = pickNewRecipe(firstElve)
        secondElve = pickNewRecipe(secondElve)

        while lastCheckedStartIndex + inputLength < len(scoreBoard):
            currentValue = ''.join(map(str, scoreBoard[lastCheckedStartIndex: lastCheckedStartIndex + inputLength]))
            if currentValue == input:
                print(lastCheckedStartIndex)
                exit()
            lastCheckedStartIndex += 1








# part1()
part2()
