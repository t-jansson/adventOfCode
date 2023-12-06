#Advent of Code 2023 Day 6 - 1

with open('input.txt') as input:
    times = input.readline()
    times = times.split(":")[1]
    times = times.split()
    distances = input.readline()
    distances = distances.split(":")[1]
    distances = distances.split()

print("Times:", times)
print("Distances:", distances)

