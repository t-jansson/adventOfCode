#Advent of Code 2022 Day 1 - 2

with open('input.txt') as input:
    cals = input.readlines()

calSum = [0]
index = int(0)
for cal in cals:
    if(cal == '\n'):
        index = index + 1
        calSum.append(0)
    else:
        calSum[index] = calSum[index] + int(cal)

calSum.sort(reverse=1)
topThree = calSum[0] + calSum[1] + calSum[2]
print(topThree)
