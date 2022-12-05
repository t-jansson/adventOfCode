#Advent of Code 2022 Day 3 - 2

with open('input.txt') as input:
    input = input.readlines()
    input = [items.strip() for items in input]

sum = 0

for i in range(0,len(input)):
    if i % 3 != 0 : continue
    if i + 2 > len(input) : break
    c1 = input[i]
    c2 = input[i+1]
    c3 = input[i+2]

    char = set(c1) & set(c2) & set(c3)
    char = str(char)[2] #Get the letter from the set
    if char.isupper(): 
        sum += ord(char) - 38
    else:
        sum += ord(char) - 96

print(sum)