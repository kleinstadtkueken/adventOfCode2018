#!/usr/bin/python3

import math

solution = 0
# param = 978
param = 10551378


for i in range(1, math.floor(math.sqrt(param)) + 1):
    #
    # for j in range(1, param + 1):
    #     r1 = i * j
    #
    #     if r1 == param:
    #         solution += i

    if param % i == 0:
        solution += param // i
        solution += i




print(solution)




# r2 = 10550400
# r4 = 10551378





