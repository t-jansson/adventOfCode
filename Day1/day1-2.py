#Advent of Code 2021 Day 1 - 2

import os, traceback

try:
    with open('Input.txt') as input:
        depths = input.readlines()

    prevValue = int(0)
    increases = int(0)
    for i in range(0, len(depths) -2):
        curVal = int(depths[i]) + int(depths[i+1]) + int(depths[i+2])
        #print(int(depths[i]), int(depths[i+1]), int(depths[i+2]), '=', curVal)
        if(prevValue != 0 and curVal > prevValue): increases += 1
        prevValue = curVal

    print('Result:', increases)

except Exception:
    traceback.print_exc()