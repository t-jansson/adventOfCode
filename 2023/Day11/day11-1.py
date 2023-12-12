#Advent of Code 2023 Day 11 - 1

import numpy

def actualSize(image: list):
    image = addSpace(image)
    image = numpy.transpose(image).tolist()
    image = addSpace(image)
    image = numpy.transpose(image).tolist()
    return image

def addSpace(image: list):
    linesToInsert = []
    for i, line in enumerate(image):
        if all(map(lambda x: x == ".", line)):
            linesToInsert.append(i)
    for j, i in enumerate(linesToInsert):
        image.insert(i+j, image[i+j])
    return image

def printImage(image: list):
    for line in image:
        print(line)

def assignNumber(image: list):
    number = 1
    numberPos = []
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] == "#":
                image[i][j] = number
                number += 1
                numberPos.append([i,j])
    return image, numberPos

def calcTotalDistance(numberPos: list):
    sum = 0
    for i in range(len(numberPos)):
        for j in range(i+1, len(numberPos)):
            sum += calcDistance(numberPos[i], numberPos[j])
    return sum

def calcDistance(pos1: list, pos2: list):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) +1 #något är fel här

def calcPairs(numbers):
    sum = 0
    for i in range(numbers):
        sum += i
    return sum

if __name__ == "__main__":

    with open('input.txt') as input:
        image = input.readlines()
        image = [s.strip() for s in image]
        image = [list(s) for s in image]

    printImage(image)
    print("")
    image = actualSize(image)
    printImage(image)
    print("")
    image, numberPos = assignNumber(image)
    printImage(image)
    print("Pairs:", calcPairs(len(numberPos)))
    result = calcTotalDistance(numberPos)
    print(result)

