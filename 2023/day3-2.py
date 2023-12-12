#Advent of Code 2023 Day 3 - 2

with open('day3_input.txt') as input:
    lines = input.readlines()

lines = [line.strip("\n") for line in lines]

sum = 0

#find all part numbers
partNbrs = []
for x in range(0, len(lines)):
    y = 0
    while y < len(lines[x]):
        partNbr = ""
        while(y < len(lines[x]) and lines[x][y].isdigit()):
            partNbr += lines[x][y]
            y += 1
        if partNbr.isdigit():
            partNbrs.append((partNbr,x,y-len(partNbr)))
            # print(partNbr)
        y += 1

#see if partnumbers have * close by
gears = []
for partNbr in partNbrs:
    for x in range(partNbr[1]-1, partNbr[1]+2):
        if x < 0 or x >= len(lines): continue
        for y in range(partNbr[2]-1, partNbr[2]+len(partNbr[0])+1):
            if y < 0 or y >= len(lines[x]): continue
            char = lines[x][y]
            if char == "*":
                # print("x,y", x,y)
                gears.append((partNbr[0],x,y))

#find valid partnumbers next to gear
for gear1 in gears:
    valid = False
    for gear2 in gears:
        if gear1[1] == gear2[1] and gear1[2] == gear2[2] and not gear1 == gear2:
            # print(gear1, gear2)
            sum += int(gear1[0]) * int(gear2[0])

sum = int(sum/2) #All gears are calculated twice, so divide by two
print("Sum:", sum)