#Advent of Code 2023 Day 2 - 1

with open('input.txt') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    line = line.split(":")
    gameID = int(line[0].split()[1])
    print(gameID)

    sets = line[1].split(";")
    for set in sets:
        red = 0
        green = 0
        blue = 0

        colors = set.split(",")

        for color in colors:
            split = color.split()
            if split[1] == "red":
                red = int(split[0])
            elif split[1] == "green":
                green = int(split[0])
            elif split[1] == "blue":
                blue = int(split[0])
    
        if(red <= 12 and green <= 13 and blue <= 14):
            print("Possible")
            print(set)
            possible = True
        else:
            print("Impossible")
            print(set)
            possible = False
            break
        
    if possible:
        sum += gameID

print("Sum:", sum)
