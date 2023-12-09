#Advent of Code 2023 Day 8 - 2

if __name__ == "__main__":

    with open('input.txt') as input:
        directions = input.readline().strip()
        input.readline() #Read empty line
        input = input.readlines()

    A = []
    B = []
    C = []
    for data in input:
        line = {}
        A.append(data[0:3])
        B.append(data[7:10])
        C.append(data[12:15])

    positions = []
    for pos in A:
        if pos[2] == 'A':
            positions.append(pos)

    # pos = 'AAA' #Start location
    target = '**Z'
    steps = 0
    while(1):
        for direction in directions:
            # print(positions, steps)
            allZ = True 
            steps += 1
            for i, pos in enumerate(positions):
                index = A.index(pos)        
                # print(direction, pos, steps)
                if direction == "L":
                    pos = B[index]
                else: #direction == "R":
                    pos = C[index]
                positions[i] = pos
                # if pos[2] == "Z": 
                #     print(pos)
                if allZ: allZ = pos[2] == "Z"
            if allZ: break
        if allZ: break

    print("Steps", steps)
        
