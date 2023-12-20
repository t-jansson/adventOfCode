#Advent of Code 2023 Day 17 - 1

def getPosValue(pos):
    return int(blocks[pos[0], pos[1]])

def calcNextPos(curPos, oldPos):
    sum()

    return newPos, curPos

if __name__ == "__main__":

    with open('day17_input.txt') as input:
        blocks = input.readlines()
        blocks = [s.strip() for s in blocks]
    
    memPos = []
    curPos = [0,0]
    oldPos = [0,0]
    while(curPos != [len(blocks[0]), len(blocks)]):
        curPos, oldPos = calcNextPos(curPos, oldPos)
        memPos.append(curPos)

    result = 0
    print(result)

