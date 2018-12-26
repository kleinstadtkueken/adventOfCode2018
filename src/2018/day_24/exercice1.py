#!/user/bin/python3
import copy
from copy import deepcopy
from typing import Dict
from enum import Enum, auto
import re


fileName = 'input.txt'
# fileName = 'example1.txt'


class Type(Enum):
    IMMUNE_SYSTEM = auto()
    INFECTION = auto()


class AttackType(Enum):
    SLASHING = 'slashing'
    BLUDGEONING = 'bludgeoning'
    FIRE = 'fire'
    COLD = 'cold'
    RADIATION = 'radiation'


class Group:
    def __init__(self, type: Type, groupId, numberOfUnits, hitPoints, weakTo, immuneTo, attackDamage, initiative, attackType: AttackType):
        self.type = type
        self.groupId = groupId
        self.numberOfUnits = numberOfUnits
        self.hitPoints = hitPoints
        self.weakTo = weakTo
        self.immuneTo = immuneTo
        self.attackDamage = attackDamage
        self.initiative = initiative
        self.attackType = attackType

    def effectivePower(self):
        return self.numberOfUnits * self.attackDamage


def parseInput():
    p = re.compile('(?P<noUnits>\d+) units each with (?P<hitPoints>\d+) hit points (?:\((?:weak to (?P<weakTo>[^;]*)|immune to (?P<immuneTo>[^;]*)|; )+\) )?with an attack that does (?P<attackDamage>\d+) (?P<attackType>[a-z]+) damage at initiative (?P<initiative>\d+)')

    groups = []
    currentType = None
    groupId = None
    with open(fileName, 'r') as file:
        for line in file:
            if line == 'Immune System:\n':
                currentType = Type.IMMUNE_SYSTEM
                groupId = 0
            elif line == 'Infection:\n':
                currentType = Type.INFECTION
                groupId = 0
            else:
                groupId += 1
                m = p.match(line[:-1])

                weakToStr = m.group('weakTo').split(',') if m.group('weakTo') else []
                weakTo = list(map(lambda s: AttackType(s.strip()), weakToStr))
                immuneToStr = m.group('immuneTo').split(',') if m.group('immuneTo') else []
                immuneTo = list(map(lambda s: AttackType(s.strip()), immuneToStr))

                groups.append(Group(currentType, groupId, int(m.group('noUnits')), int(m.group('hitPoints')), weakTo, immuneTo, int(m.group('attackDamage')), int(m.group('initiative')), AttackType(m.group('attackType'))))

    return groups


def targetSelection() -> Dict[Group, Group]:
    attackMap = dict()
    groups.sort(key=lambda t: t.initiative, reverse=True)
    groups.sort(key=lambda t: t.effectivePower(), reverse=True)

    for attacker in groups:
        powerAgainstOpponent = None
        bestOpponent = None
        for opponent in groups:
            if attacker.type != opponent.type and opponent not in attackMap.values() and attacker.attackType not in opponent.immuneTo:
                factor = 2 if attacker.attackType in opponent.weakTo else 1
                power = factor * attacker.effectivePower()

                # print(f'{attacker.type} group {attacker.groupId} would deal defending group {opponent.groupId} {power} damage')

                if bestOpponent == None or powerAgainstOpponent < power:
                    bestOpponent = opponent
                    powerAgainstOpponent = power
                elif powerAgainstOpponent == power:
                    if bestOpponent.effectivePower() < opponent.effectivePower():
                        bestOpponent = opponent
                        powerAgainstOpponent = power
                    elif bestOpponent.effectivePower() == opponent.effectivePower() and bestOpponent.initiative < opponent.initiative:
                        bestOpponent = opponent
                        powerAgainstOpponent = power

        if bestOpponent is not None:
            attackMap[attacker] = bestOpponent

    return attackMap




def attack(targets: Dict[Group, Group]):

    for attacker, opponent in sorted(targets.items(), key=lambda t: t[0].initiative, reverse=True):
        if attacker.numberOfUnits > 0:
            factor = 2 if attacker.attackType in opponent.weakTo else 1
            damage = factor * attacker.effectivePower()

            unitsKilled = damage // opponent.hitPoints

            opponent.numberOfUnits -= unitsKilled

            print(f'{attacker.type} group {attacker.groupId} attacks defending group {opponent.groupId}, killing {unitsKilled} units')


originalGroups = parseInput()
# Immune System 60
# Infection     55
boost = 59


groups = copy.deepcopy(originalGroups)

for group in groups:
    if group.type == Type.IMMUNE_SYSTEM:
        group.attackDamage += boost

while len(set(map(lambda g: g.type, groups))) > 1:
    targets = targetSelection()

    attack(targets)

    for id in range(len(groups) - 1, -1, -1):
        g = groups[id]

        if groups[id].numberOfUnits <=0:
            groups.pop(id)
        print(f'{g.type} Group {g.groupId} contains {g.numberOfUnits} units')

    print()




units = 0
for group in groups:
    print(group.numberOfUnits)
    units += group.numberOfUnits

print(f'{groups[0].type} has {units} units left')


















