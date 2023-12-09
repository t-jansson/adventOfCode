#Advent of Code 2023 Day 8 - 2

A = []
B = []
C = []

def getNewLeftPos(pos):
    return B[A.index(pos)]

def getNewRightPos(pos):
    return C[A.index(pos)]

def checkZ(pos):
    return pos[2] == "Z"

def getA(str):
    return str[0:3]

if __name__ == "__main__":

    with open('input.txt') as input:
        directions = input.readline().strip()
        input.readline() #Read empty line
        input = input.readlines()

    input.sort(key=getA)
    for data in input:
        line = {}
        A.append(data[0:3])
        B.append(data[7:10])
        C.append(data[12:15])

    positions = []
    for pos in A:
        if pos[2] == 'A':
            positions.append(pos)

    steps = 0
    while(1):
        # print(positions, steps)
        for direction in directions:
            # print(positions, steps)
            steps += 1
            # dir = direction
            if direction == "L":
                positions = list(map(getNewLeftPos, positions))
            else:
                positions = list(map(getNewRightPos, positions))
            done = all(list(map(checkZ, positions)))
            if done: break
            # if steps % 10000 == 0: print(steps, positions)
        if done: break

    print(positions)
    print("Steps", steps)
        
