#Advent of Code 2023 Day 11 - 2

import numpy

def actualSize(image: list):
    image, extraLines = addSpace(image)
    image = numpy.transpose(image).tolist()
    image, extraColumns = addSpace(image)
    image = numpy.transpose(image).tolist()
    return image, extraLines, extraColumns

def addSpace(image: list):
    linesToInsert = []
    for i, line in enumerate(image):
        if all(map(lambda x: x == ".", line)):
            linesToInsert.append(i)
    # for j, i in enumerate(linesToInsert):
    #     image.insert(i+j, image[i+j])
    return image, linesToInsert

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

def calcTotalDistance(numberPos: list, extraLines: list, extraColumns: list):
    sum = 0
    for i in range(len(numberPos)):
        for j in range(i+1, len(numberPos)):
            sum += calcDistance(numberPos[i], numberPos[j])
            sum += addExtra(numberPos[i], numberPos[j], extraLines, extraColumns)
    return sum

def addExtra(pos1, pos2, extraLines: list, extraColumns: list):
    extra = 0
    for x in extraLines:
        if pos1[0] < x < pos2[0] or pos2[0] < x < pos1[0]:
            extra += 999999 #1 000 000 extra lines (1 line already added in CalcDistance)
    for x in extraColumns:
        if pos1[1] < x < pos2[1] or pos2[1] < x < pos1[1]:
            extra += 999999 #1 000 000 extra lines (1 line already added in CalcDistance)
    return extra

def calcDistance(pos1: list, pos2: list):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

def calcPairs(numbers):
    sum = 0
    for i in range(numbers):
        sum += i
    return sum

if __name__ == "__main__":

    with open('day11_input.txt') as input:
        image = input.readlines()
        image = [s.strip() for s in image]
        image = [list(s) for s in image]

    # printImage(image)
    # print("")
    image, extraLines, extraColumns = actualSize(image)
    # printImage(image)
    # print("")
    image, numberPos = assignNumber(image)
    # printImage(image)
    # print("Pairs:", calcPairs(len(numberPos)))
    result = calcTotalDistance(numberPos, extraLines, extraColumns)
    print(result)

