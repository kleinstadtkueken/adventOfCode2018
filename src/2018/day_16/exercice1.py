#!/usr/bin/python3

from enum import Enum, auto


def parseRegister(inputStr):
    inputs = inputStr[9:-2].split(',')
    return [int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])]



class Instruction:
    def __init__(self, opcodeId, a, b, c):
        self.opcodeId = opcodeId
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def parse(inputStr):
        inputs = inputStr.split()
        return Instruction(int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3]))


class Sample:
    def __init__(self, before, instruction: Instruction, after):
        self.before = before
        self.instruction = instruction
        self.after = after
        self.validOpcodes = []


class Opcode(Enum):
    ADDR = auto()
    ADDI = auto()
    MULR = auto()
    MULI = auto()
    BANR = auto()
    BANI = auto()
    BORR = auto()
    BORI = auto()
    SETR = auto()
    SETI = auto()
    GTIR = auto()
    GTRI = auto()
    GTRR = auto()
    EQIR = auto()
    EQRI = auto()
    EQRR = auto()


    def execute(self, register, instruction: Instruction):
        after = list(register)
        if self == self.ADDR:
            # addr (add register) stores into register C the result of adding register A and register B.
            after[instruction.c] = after[instruction.a] + after[instruction.b]

        elif self == self.ADDI:
            # addi (add immediate) stores into register C the result of adding register A and value B.
            after[instruction.c] = after[instruction.a] + instruction.b

        elif self == self.MULR:
            # mulr (multiply register) stores into register C the result of multiplying register A and register B.
            after[instruction.c] = after[instruction.a] * after[instruction.b]

        elif self == self.MULI:
            # muli (multiply immediate) stores into register C the result of multiplying register A and value B.
            after[instruction.c] = after[instruction.a] * instruction.b

        elif self == self.BANR:
            #banr (bitwise AND register) stores into register C the result of the bitwise AND of register A and register B.
            after[instruction.c] = after[instruction.a] & after[instruction.b]

        elif self == self.BANI:
            # bani (bitwise AND immediate) stores into register C the result of the bitwise AND of register A and value B.
            after[instruction.c] = after[instruction.a] & instruction.b

        elif self == self.BORR:
            # borr (bitwise OR register) stores into register C the result of the bitwise OR of register A and register B.
            after[instruction.c] = after[instruction.a] | after[instruction.b]

        elif self == self.BORI:
            # bori (bitwise OR immediate) stores into register C the result of the bitwise OR of register A and value B.
            after[instruction.c] = after[instruction.a] | instruction.b

        elif self == self.SETR:
            # setr (set register) copies the contents of register A into register C. (Input B is ignored.)
            after[instruction.c] = after[instruction.a]

        elif self == self.SETI:
            # seti (set immediate) stores value A into register C. (Input B is ignored.)
            after[instruction.c] = instruction.a

        elif self == self.GTIR:
            # gtir (greater-than immediate/register) sets register C to 1 if value A is greater than register B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[instruction.a > after[instruction.b]]

        elif self == self.GTRI:
            # gtri (greater-than register/immediate) sets register C to 1 if register A is greater than value B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[after[instruction.a] > instruction.b]

        elif self == self.GTRR:
            # gtrr (greater-than register/register) sets register C to 1 if register A is greater than register B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[after[instruction.a] > after[instruction.b]]

        elif self == self.EQIR:
            # eqir (equal immediate/register) sets register C to 1 if value A is equal to register B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[instruction.a == after[instruction.b]]

        elif self == self.EQRI:
            # eqri (equal register/immediate) sets register C to 1 if register A is equal to value B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[after[instruction.a] == instruction.b]

        elif self == self.EQRR:
            # eqrr (equal register/register) sets register C to 1 if register A is equal to register B. Otherwise, register C is set to 0.
            after[instruction.c]  = {True: 1, False: 0}[after[instruction.a] == after[instruction.b]]

        return after


def part1():
    min3valid = 0
    for sample in samples:
        if len(sample.validOpcodes) >= 3:
            min3valid += 1

    print(min3valid)


samples = []
opcodes = [
    Opcode.ADDR, Opcode.ADDI,
    Opcode.MULR, Opcode.MULI,
    Opcode.BANR, Opcode.BANI,
    Opcode.BORR, Opcode.BORI,
    Opcode.SETR, Opcode.SETI,
    Opcode.GTIR, Opcode.GTRI, Opcode.GTRR,
    Opcode.EQIR, Opcode.EQRI, Opcode.EQRR
]

with open('input-A.txt', 'r') as file:
# with open('sample-A.txt', 'r') as file:
    for y, line in enumerate(file):
        if y % 4 == 0:
            before = parseRegister(line)
        elif y % 4 == 1:
            instruction = Instruction.parse(line)
        elif y % 4 == 2:
            after = parseRegister(line)
        else:
            samples.append(Sample(before, instruction, after))


for sample in samples:
    for opcode in opcodes:
        try:
            result = opcode.execute(sample.before, sample.instruction)

            if result == sample.after:
                sample.validOpcodes.append(opcode)
        except:
            pass # nothing to do here. The opcode is not possible for this sample

# part1()

# possibleOpcodes = [set() for i in range(16)]
possibleOpcodes = dict()
for i in range(16):
    possibleOpcodes[i] = set()

opcodeAssignment = [None for i in range(16)]

for sample in samples:
    possibleOpcodes[sample.instruction.opcodeId].update(sample.validOpcodes)

while len(possibleOpcodes) > 0:
    for i in range(16):
        if i in possibleOpcodes and len(possibleOpcodes[i]) == 1:
            opcodeAssignment[i] = possibleOpcodes[i].pop()
            del possibleOpcodes[i]

            for j in range(16):
                if j in possibleOpcodes and opcodeAssignment[i] in possibleOpcodes[j]:
                    possibleOpcodes[j].remove(opcodeAssignment[i])


instructions = []

with open('input-B.txt', 'r') as file:
    for line in file:
        instructions.append(Instruction.parse(line))


register = [0, 0, 0, 0]
for instruction in instructions:
    register = opcodeAssignment[instruction.opcodeId].execute(register, instruction)
print(register)


register = [0, 1, 0, 0]
for instruction in instructions:
    register = opcodeAssignment[instruction.opcodeId].execute(register, instruction)
print(register)


register = [0, 0, 1, 0]
for instruction in instructions:
    register = opcodeAssignment[instruction.opcodeId].execute(register, instruction)
print(register)


register = [7, 7, 7, 7]
for instruction in instructions:
    register = opcodeAssignment[instruction.opcodeId].execute(register, instruction)
print(register)




# print(opcodeAssignment)

