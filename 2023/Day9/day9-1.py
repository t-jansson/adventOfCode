#Advent of Code 2023 Day 9 - 1

def findNext(line):
    newLine = []
    for i in range(0, len(line)-1):
        newLine.append(line[i+1] - line[i])
    
    if not all(x == 0 for x in newLine):
        newLine.append(findNext(newLine) + newLine[-1])
    else:
        newLine.append(0)

    # print(newLine)
    return newLine[-1]

if __name__ == "__main__":

    with open('input.txt') as input:
        inputSequence = input.readlines()
        inputSequence = [s.split() for s in inputSequence]
        for i, s in enumerate(inputSequence):
            inputSequence[i] = [int(x) for x in s]

    # print(inputSequence)

    results = []
    for data in inputSequence:
        results.append(findNext(data) + data[-1])
        # print(data)

    result = sum(results)
    print(result)

