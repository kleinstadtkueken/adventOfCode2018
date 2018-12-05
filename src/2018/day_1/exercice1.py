#!/usr/bin/python3

frequency = 0

with open('input.txt', 'r') as file:
    for line in file:
        activity = line[0]
        number = line[1:]

        if activity == '+':
            frequency += int(number)
        if activity == '-':
            frequency -= int(number)


print(frequency)
