#Advent of Code 2023 Day 8 - 2

import time
network = {}


def getNewLeftPos(pos):
    return network[pos][0]

def getNewRightPos(pos):
    return network[pos][1]

def checkZ(pos):
    return pos[2] == "Z"

def getA(str):
    return str[0:3]

def checkDone(poss):
    for pos in poss:
        if pos[2] != "Z":
            return False
    return True

if __name__ == "__main__":

    with open('input.txt') as input:
        directions = input.readline().strip()
        input.readline() #Read empty line
        input = input.readlines()

    #Create dictionalry of the network
    input.sort(key=getA)
    for i, data in enumerate(input):
        network[data[0:3]] = [data[7:10], data[12:15]]

    #Get start positions
    positions = []
    for key in network.keys():
        if key[2] =="A":
            positions.append(key)

    startTime = time.time()
    steps = 0
    while(1):
        # print(positions, steps)
        for direction in directions:
            # print(positions, steps)
            steps += 1
            if direction == "L":
                positions = [network[p][0] for p in positions]
                # positions = list(map(getNewLeftPos, positions))
            else:
                positions = [network[p][1] for p in positions]
                # positions = list(map(getNewRightPos, positions))
            # done = all(list(map(checkZ, positions)))
            # done = all([p[2] == "Z" for p in positions])
            done = checkDone(positions)
            if done: break
            # if steps % 100000 == 0: print(steps, positions, time.time()-startTime)
        if done: break

    print(positions)
    print("Steps", steps)
        
