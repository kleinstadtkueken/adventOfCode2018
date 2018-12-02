#!/usr/bin/python3

exactlyTwice = 0
exactlyTrice = 0

with open('input.txt', 'r') as file:
    for line in file:
        foo = dict()

        for char in line:
            if char in foo:
                foo[char] += 1
            else:
                foo[char] = 1

        addTwice = False
        addTrice = False

        for item, count in foo.items():
            if count == 2:
                addTwice = True
            if count == 3:
                addTrice = True

        if addTwice:
            exactlyTwice += 1
        if addTrice:
            exactlyTrice += 1

print(exactlyTwice * exactlyTrice)
