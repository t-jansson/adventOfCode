#Advent of Code 2023 Day 13 - 1

from numpy import transpose
    
def findReflection(dataSet):
    for i in range(len(dataSet)-1):
        # print(dataSet[i])
        if dataSet[i] == dataSet[i+1]:
            # print("Reflection at row", i)
            k = 1
            for j in range(i+1, len(dataSet)):
                if j-k < 0:
                    print("out of range in dataset", j-k)
                elif dataSet[j] == dataSet[j-k]:
                    # print("Reflection", j, j-k)
                    if j == len(dataSet)-1 or j-k == 0:
                        # print("Real reflection at", i, i+1)
                        return i + 1
                    else:
                        k += 2
                        continue
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
        setResult = 0
        setResult += findReflection(dataSet) * 100
        dataSet = transpose(dataSet).tolist()
        setResult += findReflection(dataSet)
        # print(setResult, i)
        result += setResult

    print(result)
