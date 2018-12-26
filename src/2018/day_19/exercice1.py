#!/usr/bin/python3

from enum import Enum, auto


def parseRegister(inputStr):
    inputs = inputStr[9:-2].split(',')
    return [int(inputs[0]), int(inputs[1]), int(inputs[2]), int(inputs[3])]


class Instruction:
    def __init__(self, opcode, a, b, c):
        self.opcode = opcode
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def parse(inputStr):
        inputs = inputStr.split()
        return Instruction(Opcode[inputs[0].upper()], int(inputs[1]), int(inputs[2]), int(inputs[3]))

    def __str__(self):
        return f'{self.opcode}: a={self.a}, b={self.b}, c={self.c}'


# class Sample:
#     def __init__(self, before, instruction: Instruction, after):
#         self.before = before
#         self.instruction = instruction
#         self.after = after
#         self.validOpcodes = []


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



instructionPointerId = None
instructions = []

with open('input-A.txt', 'r') as file:
# with open('sample-A.txt', 'r') as file:
    for y, line in enumerate(file):
        if line[0] == '#':
            instructionPointerId = int(line.split()[1])
        else:
            instructions.append(Instruction.parse(line))


register = [0, 0, 0, 0, 0, 0]


while register[instructionPointerId] < len(instructions):
    register = instructions[register[instructionPointerId]].opcode.execute(register, instructions[register[instructionPointerId]])

    register[instructionPointerId] += 1




print(register)

# for instruction in instructions:
#     register = opcodeAssignment[instruction.opcodeId].execute(register, instruction)
# print(register)





# print(opcodeAssignment)

# nach einem run mit 1 [0, 10550400, 0, 0, 10551378, 0]

# nach einem run mit 0 [0, 142, 0, 1, 978, 0]


