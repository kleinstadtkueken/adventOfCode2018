#!/usr/bin/python3

from collections import namedtuple


filename = 'input.txt'
# filename = 'example2.txt'
# filename = 'example.txt'


Point = namedtuple('Point', ['x', 'y', 'z'])
Nanobot = namedtuple('Nanobot', ['point', 'radius'])

inputs = []


def part1():
    inputs.sort(key=lambda bot: bot.radius, reverse=True)

    centerBot = inputs[0]
    inRange = 0

    for bot in inputs:
        if abs(bot.point.x - centerBot.point.x) + abs(bot.point.y - centerBot.point.y) + abs(bot.point.z - centerBot.point.z) <= centerBot.radius:
            inRange += 1

    print('Part 1:', inRange)


def part2():

    inputs.sort(key=lambda bot: bot.point.x)
    minX = inputs[0].point.x
    maxX = inputs[-1].point.x

    inputs.sort(key=lambda bot: bot.point.y)
    minY = inputs[0].point.y
    maxY = inputs[-1].point.y

    inputs.sort(key=lambda bot: bot.point.z)
    minZ = inputs[0].point.z
    maxZ = inputs[-1].point.z


    diffX = maxX + abs(minX)
    diffY = maxY + abs(minY)
    diffZ = maxZ + abs(minZ)


    print()

with open(filename, 'r') as file:
    for line in file:
        parts = line.split()
        coordinats = parts[0][5:-2].split(',')

        point = Point(int(coordinats[0]), int(coordinats[1]), int(coordinats[2]))
        inputs.append(Nanobot(point, int(parts[1].split('=')[1])))

# part1()

part2()




