#Advent of Code 2023 Day 10 - 2

tiles = ()

def findStart():
    for i in range(0, len(tiles)):
        #print(tiles[i])
        for j in range(0, len(tiles[i])):
            #print(tiles[i][j])
            if tiles[i][j] == "S":
                return i,j
    return False

def findStartOptions(start):
    # print(tiles[start[0]][start[1]], start[0],start[1])

    startOptions = []

    if tiles[start[0]-1][start[1]] in {"|", "F", "7"}:
        # print(tiles[start[0]-1][start[1]], start[0]-1,start[1])
        startOptions.append([start[0]-1,start[1]])
    if tiles[start[0]][start[1]+1] in {"-", "J", "7"}:
        # print(tiles[start[0]][start[1]+1], start[0],start[1]+1)
        startOptions.append([start[0],start[1]+1])
    if tiles[start[0]+1][start[1]] in {"|", "L", "J"}:
        # print(tiles[start[0]+1][start[1]], start[0]+1,start[1])
        startOptions.append([start[0]+1,start[1]])
    if tiles[start[0]][start[1]-1] in {"-", "L", "F"}:
        # print(tiles[start[0]][start[1]-1], start[0],start[1]-1)
        startOptions.append([start[0],start[1]-1])
    
    if len(startOptions) == 2:
        return startOptions
    else:
        print("Error at start", startOptions)

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

def findNextLocation(old, current):
    if old == current:
        print("ERROR", old, current)
    # print(tiles[current[0]][current[1]])
    match tiles[current[0]][current[1]]:
        case "|":
            if old[0] < current[0]:
                nextLocation = [current[0] + 1, current[1]]
            else:
                nextLocation = [current[0] - 1, current[1]]
        case "-":
            if old[1] < current[1]:
                nextLocation = [current[0], current[1] + 1]
            else:
                nextLocation = [current[0], current[1] - 1]
        case "L":
            if old[0] < current[0]:
                nextLocation = [current[0], current[1] + 1]
            else:
                nextLocation = [current[0] - 1, current[1]]
        case "J":
            if old[0] < current[0]:
                nextLocation = [current[0], current[1] - 1]
            else:
                nextLocation = [current[0] - 1, current[1]]
        case "7":
            if old[0] > current[0]:
                nextLocation = [current[0], current[1] - 1]
            else:
                nextLocation = [current[0] + 1, current[1]]
        case "F":
            if old[0] > current[0]:
                nextLocation = [current[0], current[1] + 1]
            else:
                nextLocation = [current[0] + 1, current[1]]
        case ".":
            print("GROUND!", current)
        case "S":
            print("START", current)
        case _:
            print("What the fudge!", current)
    return nextLocation

def printAllPos(allPos):
    newTiles = list(tiles)
    for pos in allPos:
        newTiles[pos[0]] = str(newTiles[pos[0]][:pos[1]]) + "*" + str(newTiles[pos[0]][pos[1]+1:])

    for tile in newTiles:
        print(tile)

    return newTiles

def printAllNotPos(allPos):
    newTiles = ["0"*len(tiles[0]) for i in range(len(tiles))]
    
    for pos in allPos:
        newTiles[pos[0]] = str(newTiles[pos[0]][:pos[1]]) + str(tiles[pos[0]][pos[1]]) + str(newTiles[pos[0]][pos[1]+1:])

    for tile in newTiles:
        print(tile)

    return newTiles

if __name__ == "__main__":

    with open('input.txt') as input:
        temp = input.readlines()
        temp = [s.strip() for s in temp]
    tiles = tuple(temp)
    # print(tiles)

    allPos = []
    start = findStart()
    allPos.append(list(start))    
    steps = 0
    oldPos = [start, start]
    curPos = findStartOptions(start)
    newPos = [0,0]
    steps += 1
    while curPos[0] != curPos[1]:
        allPos.append(curPos[0])
        allPos.append(curPos[1])
        # print(curPos[0])
        newPos[0] = findNextLocation(oldPos[0], curPos[0])
        # print(newPos[0])
        # print(curPos[1])
        newPos[1] = findNextLocation(oldPos[1], curPos[1])
        # print(newPos[1])
        oldPos = tuple(curPos)
        curPos = tuple(newPos)
        steps += 1

    allPos.append(curPos[0])
    # printAllPos(allPos)
    printAllNotPos(allPos)
    # print(steps)