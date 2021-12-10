#Advent of Code 2021 Day 2 - 1

import os, traceback

with open('Input.txt') as input:
    commands = input.readlines()

exit()
depth = int(0)
position = int(0)
for command in commands:
    if('forward' in command):
        print('add value to position')
        position += 1
    if('down' in command):
        print('decrease position')
        depth -= 1
    if('up' in command):
        print('increase position')
        depth += 1

print('Depth:', depth, 'Position:', position)
print('Result:', int(depth) * int(position))
