#Advent of Code 2022 Day 1 - 1

with open('input.txt') as input:
    cals = input.readlines()

calSum = 0
mostCal = 0
for cal in cals:
    if(cal == '\n'):
        if(calSum > mostCal):
            mostCal = calSum
        calSum = 0
    else:
        calSum = calSum + int(cal)

print(mostCal)
