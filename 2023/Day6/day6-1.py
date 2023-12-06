#Advent of Code 2023 Day 6 - 1

import numpy

def calc(time, distance):
    wins = []
    for x in range(1,time+1):
        if x * (time - x) > distance:
            wins.append(x)
    return len(wins)

with open('input.txt') as input:
    times = input.readline()
    times = times.split(":")[1]
    times = times.split()
    times = [int(i) for i in times]
    distances = input.readline()
    distances = distances.split(":")[1]
    distances = distances.split()
    distances = [int(i) for i in distances]



print("Times:", times)
print("Distances:", distances)

wins = []
for x in range(0, len(times)):
    wins.append(calc(times[x], distances[x]))

result = numpy.prod(wins)

print(wins)
print(result)