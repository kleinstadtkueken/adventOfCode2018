#!/usr/bin/python3

frequency = 0
seenFrequencies = {frequency}

for i in range(1000):
    with open('input.txt', 'r') as file:
        for line in file:
            activity = line[0]
            number = line[1:]

            if activity == '+':
                frequency += int(number)
            if activity == '-':
                frequency -= int(number)

            if frequency in seenFrequencies:
                print(frequency)
                print(i)
                exit(0)

            seenFrequencies.add(frequency)

print('not found')
