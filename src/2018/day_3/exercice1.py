#!/usr/bin/python3


class Claim:

    def __init__(self, id, start_x, start_y, width, height):
        self.id = id
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height


fabric = [[0 for j in range(1000)] for i in range(1000)]
input = []


with open('input.txt', 'r') as file:
    for line in file:
        parts = line.split(' ')
        start = parts[2][:-1].split(',')
        dim = parts[3][:-1].split('x')

        input.append(Claim(parts[0][1:], int(start[0]), int(start[1]), int(dim[0]), int(dim[1])))


for item in input:

    for y in range(item.start_y, item.start_y + item.height):
        for x in range(item.start_x, item.start_x + item.width):
            fabric[x][y] += 1

overlap = 0

for i in fabric:
    for j in i:
        if j > 1:
            overlap += 1

print(overlap)



