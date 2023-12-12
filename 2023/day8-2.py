#Advent of Code 2023 Day 8 - 2

import time
import itertools
import math

if __name__ == "__main__":

    with open('day8_input.txt') as input:
        directions = input.readline().strip()
        input.readline() #Read empty line
        input = input.readlines()

    #Create dictionalry of the network
    network = {}        
    for data in input:
        network[data[0:3]] = [data[7:10], data[12:15]]

    #Get start positions
    positions = []
    for key in network.keys():
        if key.endswith("A"):
            positions.append(key)

    results = [0] * len(positions)
    startTime = time.time()
    for steps, direction in enumerate(itertools.chain.from_iterable(itertools.repeat(directions)), start=1):

        index = 0 if direction == "L" else 1

        for i, position in enumerate(positions):
            positions[i] = network[position][index]

            if positions[i].endswith("Z"):
                results[i] = steps

        if all([result > 0 for result in results]):
            break

    result = math.lcm(*results)

    print("Steps", result)
    print("Time:", time.time()-startTime)
