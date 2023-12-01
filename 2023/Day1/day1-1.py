#Advent of Code 2023 Day 1 - 1

import string

with open('input.txt') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    firstDigit = None
    lastDigit = None
    for i in range(0, len(line)):
        char = line[i]
        if char.isdigit():
            if firstDigit == None:
                firstDigit = char
            else:
                lastDigit = char
    if lastDigit != None:
        lineDigit = int(firstDigit + lastDigit)
    else:
        lineDigit = int(firstDigit + firstDigit)
        
    sum += lineDigit

print(sum)
