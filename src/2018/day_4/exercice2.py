#!/usr/bin/python3

from datetime import datetime


class Log:

    def __init__(self, date, activity):
        self.thedate = date
        self.activity = activity


class Shift:

    def __init__(self, guardId, shiftStart):
        self.guardId = guardId
        self.shiftStart = shiftStart
        self.sleepCycle = []


input = []


with open('input.txt', 'r') as file:
    for line in file:
        date = datetime.strptime(line[1:17], '%Y-%m-%d %H:%M')

        input.append(Log(date, line[19:-1]))

input.sort(key=lambda log: log.thedate)


i = 0
shifts = []
while i < len(input):
    id = input[i].activity.split(' ')[1][1:]
    shift = Shift(id, input[i].thedate)
    shifts.append(shift)
    i += 1

    while i < len(input) and input[i].activity == 'falls asleep':
        shift.sleepCycle.append((input[i].thedate, input[i + 1].thedate))
        i += 2


# map sleep times for each guard between 00:00 and 00:59
asleep = {}

for shift in shifts:
    if shift.guardId not in asleep:
        asleep[shift.guardId] = [0 for i in range(60)]

    for cycle in shift.sleepCycle:
        (start, end) = cycle

        for min in range(start.minute, end.minute):
            asleep[shift.guardId][min] += 1


# find max asleep min
guardId = None
timesSlept = 0
minute = None


for id, sleep in asleep.items():
    if timesSlept < max(sleep):
        guardId = id
        timesSlept = max(sleep)
        for i in range(60):
            if sleep[i] == timesSlept:
                maxMin = i


print(maxMin * int(guardId))
