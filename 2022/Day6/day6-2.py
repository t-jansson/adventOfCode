#Advent of Code 2022 Day 6 - 2

with open('input.txt') as input:
    buffer = input.readline()
    

for i in range(14,len(buffer)):
    SOP = buffer[i-14:i]
    SOP = set(SOP)
    if len(SOP) == 14:
        marker = i
        break

print(marker)