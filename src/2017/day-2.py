#!/usr/bin/python3

input = []

with open('day-2.txt', 'r') as file:
    for line in file:
        input.append([int(x) for x in line.split()])


checksum1 = 0

for line in input:
    checksum1 += max(line) - min(line)

print(checksum1)


checksum2 = 0

for line in input:
    for i in range(len(line) - 1):
        for j in range(i + 1, len(line)):
            if line[i] > line[j]:
                if line[i] % line[j] == 0:
                    checksum2 += line[i] // line[j]
            else:
                if line[j] % line[i] == 0:
                    checksum2 += line[j] // line[i]

print(checksum2)

