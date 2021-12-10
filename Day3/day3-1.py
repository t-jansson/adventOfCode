#Advent of Code 2021 Day 2 - 1

import os, traceback
from typing import Counter

with open('Input.txt') as input:
    report = input.readlines()

Counter = [0] * (len(report[0])-1)
for line in report:
    for i in range(0, len(line)-1):
        Counter[i] = Counter[i] + int(line[i])

print(Counter)

gamma = [0] * (len(Counter)-1)
epsilon = [0] * (len(Counter)-1)
for i in range(0, len(Counter)-1):
    if(Counter[i] > len(report) / 2):
        gamma[i] = '1'
        epsilon[i] = '0'
    else:
        gamma[i] = '0'
        epsilon[i] = '1'

gammaValue = int(''.join(str(i) for i in gamma), 2)
epsilonValue = int(''.join(str(i) for i in epsilon), 2)

print('Gamma:', gamma, 'Val:', gammaValue)
print('Epsilon:', epsilon, 'Val:', epsilonValue)

result = gammaValue * epsilonValue

print('Result:', result)
