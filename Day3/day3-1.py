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

gamma = [0] * (len(Counter[0])-1)
epsilon = [0] * (len(Counter[0])-1)
for i in range(0, len(Counter)-1):
    if(Counter[i] > 500):
        gamma[i] = 1
        epsilon[i] = 0
    else:
        gamma[i] = 0
        epsilon[i] = 1

print('Gamma:', gamma)
print('Epsilon:', epsilon)



print('Result:', int(gamma) * int(epsilon))
