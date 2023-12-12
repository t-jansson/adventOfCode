#Advent of Code 2023 Day 10 - 2

tiles = ()

def findStart():
    for i in range(0, len(tiles)):
        for j in range(0, len(tiles[i])):
            if tiles[i][j] == "S":
                return i,j
    return False

def findStartOptions(start):
    startOptions = []
    if tiles[start[0]-1][start[1]] in {"|", "F", "7"}:
        startOptions.append([start[0]-1,start[1]])
    if tiles[start[0]][start[1]+1] in {"-", "J", "7"}:
        startOptions.append([start[0],start[1]+1])
    if tiles[start[0]+1][start[1]] in {"|", "L", "J"}:
        startOptions.append([start[0]+1,start[1]])
    if tiles[start[0]][start[1]-1] in {"-", "L", "F"}:
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
    newTiles = ["*"*len(tiles[0]) for i in range(len(tiles))]
    for pos in allPos:
        newTiles[pos[0]] = str(newTiles[pos[0]][:pos[1]]) + str(tiles[pos[0]][pos[1]]) + str(newTiles[pos[0]][pos[1]+1:])
    for tile in newTiles:
        print(tile)
    return newTiles

def checkReplace(tiles, tile, i, j):
    if i == 0 or i == len(tiles)-1:
        return True
    if j == 0 or j == len(tile)-1:
        return True
    if j > 0:
        if tile[j-1] == "0":
            return True
    if j < len(tile)-1:
        if tile[j+1] == "0":
            return True
    if i > 0:
        if tiles[i-1][j] == "0":
            return True
    if i < len(tiles)-1:
        if tiles[i+1][j] == "0":
            return True
    return False

def markNotLoop(newTiles):
    while True:
        count = 0
        for i, tile in enumerate(newTiles):
            for j in range(0, len(tile)):
                if tile[j] == "*" and checkReplace(newTiles, tile, i, j):
                    tile = str(tile[:j]) + "0" + str(tile[j+1:])
                    count += 1
            newTiles[i] = tile
        
        for i, tile in reversed(list(enumerate(newTiles))):
            for j in range(len(tile)-1, 0, -1):
                if tile[j] == "*" and checkReplace(newTiles, tile, i, j):
                    tile = str(tile[:j]) + "0" + str(tile[j+1:])
                    count += 1
            newTiles[i] = tile
        if count == 0:
            break
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
    newTiles = printAllNotPos(allPos)
    # print(steps)
    print("")

    newTiles = markNotLoop(newTiles)

    for tile in newTiles:
        print(tile)

    result = 0
    for tile in newTiles:
        counter = tile.count("*")
        result += counter
    print(result)