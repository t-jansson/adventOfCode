#Advent of Code 2023 Day 2 - 2

with open('day2_input.txt') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    line = line.split(":")
    gameID = int(line[0].split()[1])
    # print(gameID)

    red = 0
    green = 0
    blue = 0
    sets = line[1].split(";")
    for set in sets:
        colors = set.split(",")

        for color in colors:
            split = color.split()
            if split[1] == "red":
                if int(split[0]) > red:
                    red = int(split[0])
            elif split[1] == "green":
                if int(split[0]) > green:
                    green = int(split[0])
            elif split[1] == "blue":
                if int(split[0]) > blue:
                    blue = int(split[0])
    
    sum += red * green * blue

print("Sum:", sum)
