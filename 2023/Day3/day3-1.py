#Advent of Code 2023 Day 3 - 1

with open('input.txt') as input:
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

#see if partnumbers have symbols close by
for partNbr in partNbrs:
    print(partNbr[0], partNbr[1], partNbr[2])
    valid = False
    for x in range(partNbr[1]-1, partNbr[1]+2):
        if x < 0 or x >= len(lines): continue
        # print("x", x)
        for y in range(partNbr[2]-1, partNbr[2]+len(partNbr[0])+1):
            if y < 0 or y >= len(lines[x]): continue
            # print("y", y)
            # print("x,y", x,y)
            char = lines[x][y]
            if not char.isdigit() and not char == ".":
                valid = True
                # print(char)
            if valid:
                break
        if valid:
            break
    if valid:
        sum += int(partNbr[0])

print("Sum:", sum)