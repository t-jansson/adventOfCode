#Advent of Code 2021 Day 1 -

import os, traceback

try:
    with open('Input.txt') as input:
        depths = input.readlines()

    prevValue = 0
    increases = 0
    for depth in depths:
        if(prevValue != 0 and int(depth) > int(prevValue)): increases += 1
        prevValue = depth

    print(increases)

except Exception:
    traceback.print_exc()