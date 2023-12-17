#Advent of Code 2023 Day 14 - 1

from numpy import transpose
    
if __name__ == "__main__":

    with open('day14_input.txt') as input:
        platform = [i.strip() for i in input.readlines()]
        platform = [list(i) for i in platform]

    for row in platform:
        print(row)

    print("")
    platform90 = transpose(platform).tolist

    for row in platform90:
        print(row)

    # dataSets = []
    # data = []
    # for i, row in enumerate(input):
    #     row = row.replace("#", "1")
    #     row = row.replace(".", "0")
    #     row = row.replace("O", "2")
    #     row = [int(x) for x in row]
    #     if row == []:
    #         dataSets.append(data)
    #         data = []
    #     elif i == len(input) -1:
    #         data.append(row)
    #         dataSets.append(data)
    #     else:
    #         data.append(row)

    # for set in dataSets:
    #     print(set)