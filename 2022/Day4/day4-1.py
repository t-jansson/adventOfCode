#Advent of Code 2022 Day 4 - 1

with open('input.txt') as input:
    input = input.readlines()

sum = 0 #Nr of overlapping pairs

for pairs in input:
    pairs = pairs.strip()
    pairs = pairs.split(',')
    
    p1 = pairs[0].split('-')
    p2 = pairs[1].split('-')

    p1 = set(list(range(int(p1[0]),int(p1[1])+1)))
    p2 = set(list(range(int(p2[0]),int(p2[1])+1)))

    if p1.issubset(p2) or p2.issubset(p1):
        sum += 1
        print(pairs)

print(sum)