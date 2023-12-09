#Advent of Code 2023 Day 8 - 1

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

    pos = 'AAA' #Start location
    target = 'ZZZ'
    index = A.index(pos)
    steps = 0
    while(pos != target):
        for direction in directions:
            steps += 1
            print(direction, pos, steps)
            if direction == "L":
                pos = B[index]
                if pos == target: break
                index = A.index(pos)
            elif direction == "R":
                pos = C[index]
                if pos == target: break
                index = A.index(pos)
            else: 
                print("Something when wrong")
                pos = target #To stop while loop
                break
        
    print("Steps", steps)
        
