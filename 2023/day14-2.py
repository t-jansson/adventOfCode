#Advent of Code 2023 Day 14 - 2

from numpy import transpose
    
def countRocks(platform):
    sum = 0
    for i, row in enumerate(platform):
        sum += row.count("O") * (len(platform) - i)
    return sum

def tiltPlatform(platform):
    platform90 = transpose(platform).tolist()
    for row in platform90:
        tiltRow(row)
    platform = transpose(platform90).tolist()
    return platform

def tiltRow(row):
    for i, char in enumerate(row):
        if char == ".":
            for j in range(i+1, len(row)):
                if row[j] == "#":
                    break
                elif row[j] == "O":
                    row[i] = "O"
                    row[j] = "."
                    break

def rotateRight(platform):
    rotated = tuple(zip(*platform[::-1]))
    return rotated

if __name__ == "__main__":

    with open('day14_input.txt') as input:
        platform = [i.strip() for i in input.readlines()]
        platform = [list(i) for i in platform]

    memoryi = {}
    memoryOffset = {}
    for i in range(1000000000-1):
        platform = tiltPlatform(platform)

        platform = tiltPlatform(rotateRight(platform))

        platform = tiltPlatform(rotateRight(platform))

        platform = tiltPlatform(rotateRight(platform))

        platform = rotateRight(platform)
        if platform in memoryi:
            print(i)
            if platform not in memoryOffset:
                memoryOffset[platform] = i - memoryi[platform]
        else:
            memoryi[platform] = i


    result = countRocks(platform)
    print(result)