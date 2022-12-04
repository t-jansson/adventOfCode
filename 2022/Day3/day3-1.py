#Advent of Code 2022 Day 3 - 1

with open('input.txt') as input:
    input = input.readlines()

sum = 0

for items in input:
    items = items.strip()
    c1 = items[0:int(len(items)/2)]
    c2 = items[int(len(items)/2):]

    char = list(set(c1) & set(c2))
    if char[0].isupper(): 
        sum += ord(char[0]) - 38
    else:
        sum += ord(char[0]) - 96

print(sum)