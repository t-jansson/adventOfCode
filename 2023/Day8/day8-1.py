#Advent of Code 2023 Day 8 - 1

import itertools

if __name__ == "__main__":

    with open('input.txt') as input:
        directions = input.readline().strip()
        input.readline() #Read empty line
        input = input.readlines()


    #Create dictionalry of the network
    network = {}        
    for data in input:
        network[data[0:3]] = [data[7:10], data[12:15]]

    pos = 'AAA' #Start location
    target = 'ZZZ'
    steps = 0
    for steps, direction in enumerate(itertools.chain.from_iterable(itertools.repeat(directions)), start=1):
        # print(direction, pos, steps)
        
        index = 0 if direction == "L" else 1
        pos = network[pos][index]
        if pos == target: break

    print("Steps", steps)
        
