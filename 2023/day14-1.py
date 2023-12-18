#Advent of Code 2023 Day 14 - 1

from numpy import transpose
    
def countRocks(platform):
    sum = 0
    for i, row in enumerate(platform):
        sum += row.count("O") * (len(platform) - i)
    return sum


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

if __name__ == "__main__":

    with open('day14_input.txt') as input:
        platform = [i.strip() for i in input.readlines()]
        platform = [list(i) for i in platform]

    platform90 = transpose(platform).tolist()

    for row in platform90:
        line = ["".join(s) for s in row]
        tiltRow(row)

    platform = transpose(platform90).tolist()

    for row in platform:
        line = ["".join(s) for s in row]

    result = countRocks(platform)
    print(result)