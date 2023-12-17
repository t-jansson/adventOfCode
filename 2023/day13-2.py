#Advent of Code 2023 Day 13 - 2

from numpy import transpose
    
def compareRows(r1, r2):
    smudges = 0
    for i in range(len(r1)):
        if r1[i] - r2[i] != 0:
            smudges += 1
            if smudges > 1:
                break
    return smudges

def findReflection(dataSet):
    for i in range(len(dataSet)-1):
        nbrOfSmudges = 0
        # print(dataSet[i])
        if compareRows(dataSet[i], dataSet[i+1]) <= 1:
            k = 1
            for j in range(i+1, len(dataSet)):
                if j-k < 0:
                    print("out of range in dataset", j-k) #Should not happen...
                    break
                nbrOfSmudges += compareRows(dataSet[j], dataSet[j-k])
                if nbrOfSmudges <= 1:
                    # print("Reflection", j, j-k)
                    if j == len(dataSet)-1 or j-k == 0:
                        # print("Real reflection at", i, i+1)
                        if nbrOfSmudges == 1:
                            return i + 1 
                        else:
                            break
                    else:
                        k += 2
                else:
                    break
    return 0
    
if __name__ == "__main__":

    with open('day13_input.txt') as input:
        input = [i.strip() for i in input.readlines()]

    dataSets = []
    data = []
    for i, row in enumerate(input):
        row = row.replace("#", "1")
        row = row.replace(".", "0")
        row = [int(x) for x in row]
        if row == []:
            dataSets.append(data)
            data = []
        elif i == len(input) -1:
            data.append(row)
            dataSets.append(data)
        else:
            data.append(row)

    result = 0
    for i, dataSet in enumerate(dataSets):
        result += findReflection(dataSet) * 100
        dataSet = transpose(dataSet).tolist()
        result += findReflection(dataSet)

    print(result)
