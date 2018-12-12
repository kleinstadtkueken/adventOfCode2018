#!/usr/bin/python

mem = [11,11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
seenStates = dict()
cycleNo = 0
seenStates[mem.__str__()] = cycleNo

while True:
    cycleNo += 1
    maxBlocks = max(mem)
    currentBlock = 0
    for i, blocks in enumerate(mem):
        if blocks == maxBlocks:
            currentBlock = i
            break

    mem[currentBlock] = 0

    for _ in range(maxBlocks):
        currentBlock = (currentBlock + 1) % len(mem)
        mem[currentBlock] += 1

    if mem.__str__() in seenStates:
        print(cycleNo)
        print(cycleNo - seenStates[mem.__str__()])
        break
    else:
        seenStates[mem.__str__()] = cycleNo




