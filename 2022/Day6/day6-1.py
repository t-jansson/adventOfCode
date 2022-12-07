#Advent of Code 2022 Day 5 - 1

with open('input.txt') as input:
    buffer = input.readline()
    

for i in range(4,len(buffer)):
    SOP = buffer[i-4:i]
    SOP = set(SOP)
    if len(SOP) == 4:
        marker = i
        break

print(marker)