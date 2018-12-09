#!/usr/bin/python3


class Step:
    def __init__(self, name, stepAfter):
        self.name = name
        self.stepsAfter = []
        if stepAfter is not None:
            self.stepsAfter = [stepAfter]
        self.stepsBefore = set()


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
            input[stepAfter] = Step(name, None)


for name, step in input.items():
    for stepAfter in step.stepsAfter:
        input[stepAfter].stepsBefore.add(name)

availableSteps = findAvailableSteps()

while len(availableSteps) > 0:
    availableSteps.sort()

    current = availableSteps.pop(0)
    result += current

    for step in input[current].stepsAfter:
        input[step].stepsBefore.remove(current)

    del(input[current])
    availableSteps = findAvailableSteps()

print(result)
