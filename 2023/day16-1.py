#Advent of Code 2023 Day 16 - 1

memCord = set()

def getNewPosDir(curX, curY, direction: str):
    match grid[curX][curY]:
        case ".":
            match direction:
                case "up":
                    return (curX-1, curY), "up", (-1,-1), "NA"
                case "down":
                    return (curX+1, curY), "down", (-1,-1), "NA"
                case "right":
                    return (curX, curY+1), "right", (-1,-1), "NA"
                case "left":
                    return (curX, curY-1), "left", (-1,-1), "NA"
        case "|":
            match direction:
                case "up":
                    return (curX-1, curY), "up", (-1,-1), "NA"
                case "down":
                    return (curX+1, curY), "down", (-1,-1), "NA"
                case "right":
                    #split beam down
                    return (curX-1, curY), "up", (curX+1, curY), "down"
                case "left":
                    #split beam up
                    return (curX+1, curY), "down", (curX-1, curY), "up"
        case "-":
            match direction:
                case "up":
                    #split beam left
                    return (curX, curY+1), "right", (curX, curY-1), "left"
                case "down":
                    #split beam right
                    return (curX, curY-1), "left", (curX, curY+1), "right"
                case "right":
                    return (curX, curY+1), "right", (-1,-1), "NA"
                case "left":
                    return (curX, curY-1), "left", (-1,-1), "NA"
        case "/":
            match direction:
                case "up":
                    return (curX, curY+1), "right", (-1,-1), "NA"
                case "down":
                    return (curX, curY-1), "left", (-1,-1), "NA"
                case "right":
                    return (curX-1, curY), "up", (-1,-1), "NA"
                case "left":
                    return (curX+1, curY), "down", (-1,-1), "NA"
        case "\\":
            match direction:
                case "up":
                    return (curX, curY-1), "left", (-1,-1), "NA"
                case "down":
                    return (curX, curY+1), "right", (-1,-1), "NA"
                case "right":
                    return (curX+1, curY), "down", (-1,-1), "NA"
                case "left":
                    return (curX-1, curY), "up", (-1,-1), "NA"


if __name__ == "__main__":

    with open('day16_input.txt') as input:
        grid = input.readlines()
        grid = [s.strip() for s in grid]
    
    beams = [[(0,0), "right"]]
    for beam in beams:
        curPos = beam[0]
        curDir = beam[1]
        while(0 <= curPos[0] < len(grid[0]) and 0 <= curPos[1] < len(grid)):
            memCord.add((curPos, curDir))
            curPos, curDir, splitPos, splitDir = getNewPosDir(curPos[0], curPos[1], curDir)
            if splitDir != "NA":
                beams.append([splitPos, splitDir])
            if (curPos, curDir) in memCord:
                break

    cords = set()
    for cord in memCord:
        cords.add(cord[0])

    result = len(cords)
    print(result)

