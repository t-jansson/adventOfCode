#Advent of Code 2023 Day 6 - 2

def calc(time, distance):
    wins = 0
    for x in range(1, time+1):
        if x * (time - x) > distance:
            wins += 1
    return wins

with open('day6_input.txt') as input:
    times = input.readline()
    times = times.split(":")[1]
    times = times.split()
    time = "".join(times)
    distances = input.readline()
    distances = distances.split(":")[1]
    distances = distances.split()
    distance = "".join(distances)

print("Times:", time)
print("Distances:", distance)

win = calc(int(time), int(distance))

print(win)