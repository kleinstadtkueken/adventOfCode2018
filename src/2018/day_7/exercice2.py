#!/usr/bin/python3


class Step:
    def __init__(self, name, stepAfter):
        self.name = name
        self.stepsAfter = []
        if stepAfter is not None:
            self.stepsAfter = [stepAfter]
        self.stepsBefore = set()

class Worktask:
    def __init__(self, name):
        self.name = name
        self.remainingDuration = 60 + ord(name) - ord('A') + 1


def findAvailableSteps():
    available = []
    for name, step in input.items():
        if len(step.stepsBefore) == 0:
            available.append(name)
    return available


input = dict()
result = ''

with open('input.txt', 'r') as file:
    for line in file:
        c = line.split(' ')
        name, stepAfter = c[1], c[7]

        if name not in input:
            input[name] = Step(name, stepAfter)
        else:
            input[name].stepsAfter.append(stepAfter)

        if stepAfter not in input:
            input[stepAfter] = Step(stepAfter, None)

for name, step in input.items():
    for stepAfter in step.stepsAfter:
        input[stepAfter].stepsBefore.add(name)

availableSteps = findAvailableSteps()
availableSteps.sort()
workers = [None for i in range(5)]
currentSec = -1


while len(input) > 0:
    currentSec += 1

    for i in range(5):
        if workers[i] is not None:
            workers[i].remainingDuration -= 1

            if workers[i].remainingDuration == 0:
                current = workers[i].name
                workers[i] = None
                result += current

                for step in input[current].stepsAfter:
                    input[step].stepsBefore.remove(current)

                del(input[current])

    availableSteps = findAvailableSteps()
    for worker in workers:
        if worker is not None and worker.name in availableSteps:
            availableSteps.remove(worker.name)
    availableSteps.sort()

    for i in range(5):
        if workers[i] is None and len(availableSteps) > 0:
            workers[i] = Worktask(availableSteps.pop(0))


print(result, currentSec)
