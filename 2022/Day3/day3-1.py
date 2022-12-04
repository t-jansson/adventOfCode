#Advent of Code 2022 Day 3 - 1

with open('input.txt') as input:
    input = input.readlines()

sum = 0

for items in input:
    items = items.strip()
    fCompartment = items[0:int(len(items)/2)]
    sCompartment = items[int(len(items)/2):]

    for char in fCompartment:
        if sCompartment.find(char) > 0:
            value = ord(char.lower()) - 96
            if char.isupper():
                value = value + 26
            sum = sum + value
            break

print(sum)