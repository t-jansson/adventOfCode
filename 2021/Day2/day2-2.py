#Advent of Code 2021 Day 2 - 2

import os, traceback

with open('Input.txt') as input:
    commands = input.readlines()

depth = int(0)
position = int(0)
aim = int(0)
for command in commands:
    if('forward' in command):
        #print('add value to position')
        line = command.split(' ')
        position += int(line[1])
        depth += aim * int(line[1])
    if('down' in command):
        #print('decrease position')
        line = command.split(' ')
        aim += int(line[1])
    if('up' in command):
        #print('increase position')
        line = command.split(' ')
        aim -= int(line[1])

print('Depth:', depth, 'Position:', position)
print('Result:', int(depth) * int(position))
