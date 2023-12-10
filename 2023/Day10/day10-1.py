#Advent of Code 2023 Day 10 - 1

tiles = ()

def findStart():
    for i in range(0, len(tiles)):
        print(tiles[i])
        for j in range(0, len(tiles[i])):
            print(tiles[i][j])
            if tiles[i][j] == "S":
                return i,j
    return False


# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def getNewLocation(old, current):
    match tiles[current[0], current[1]]:
        case "|":
            if old[0] < current[0]:
                newLocation = [current[0] + 1, current[1]]
            else:
                newLocation = [current[0] - 1, current[1]]
        case "-":
            if old[1] < current[1]:
                newLocation = [current[0], current[1] + 1]
            else:
                newLocation = [current[0], current[1] - 1]

        case "L":
            if old[0] < current[0]:
                newLocation = [current[0], current[1] + 1]
            else:
                newLocation = [current[0] - 1, current[1]]


if __name__ == "__main__":

    with open('input.txt') as input:
        temp = input.readlines()
        temp = [s.strip() for s in temp]
    tiles = tuple(temp)
        
print(tiles)
print(findStart())