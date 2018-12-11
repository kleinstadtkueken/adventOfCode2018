#!/usr/bin/python3

steps = 0
commands = []

with open('day-5.txt', 'r') as file:
    for line in file:
        commands.append(int(line))

current = 0

while 0 <= current < len(commands):
    next = current + commands[current]
    if commands[current] >= 3:
        commands[current] -= 1
    else:
        commands[current] += 1

    current = next
    steps += 1



print(steps)


