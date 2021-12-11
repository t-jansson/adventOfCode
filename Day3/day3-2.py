#Advent of Code 2021 Day 3 - 2

with open('Input.txt') as input:
    report = input.readlines()


oxygenData = [line.strip('\n') for line in report]
for i in range(0, len(oxygenData[0])):
    if(len(oxygenData) == 1):
        break
    counter = int(0)
    length = len(oxygenData)
    # print('Length:', length)
    for data in oxygenData:
        if(data[i] == '1'):
            counter += 1
    # print('Counter:', counter)
    if(counter >= length / 2):
        mostCommon = '1'
    else:
        mostCommon = '0'
    # print('MostCommon:', mostCommon)
    newData = []
    for data in oxygenData:
        if(data[i] == mostCommon):
            # print(i, data)
            newData.append(data)
    oxygenData = newData
oxygenValue = int(''.join(str(i) for i in oxygenData), 2)
print(oxygenData, oxygenValue)

co2Data = [line.strip('\n') for line in report]
for i in range(0, len(co2Data[0])):
    if(len(co2Data) == 1):
        break
    counter = int(0)
    length = len(co2Data)
    # print('Length:', length)
    for data in co2Data:
        if(data[i] == '1'):
            counter += 1
    # print('Counter:', counter)
    if(counter >= length / 2):
        mostCommon = '0'
    else:
        mostCommon = '1'
    # print('MostCommon:', mostCommon)
    newData = []
    for data in co2Data:
        if(data[i] == mostCommon):
            # print(i, data)
            newData.append(data)
    co2Data = newData
co2Value = int(''.join(str(i) for i in co2Data), 2)
print(co2Data, co2Value)

print('Result:', oxygenValue * co2Value)


# for data in oxygenData:
#     if(counter > length / 2):
            

# # New list with only the common bit

# Counter = [0] * (len(report[0])-1)
# for line in report:
#     for i in range(0, len(line)-1):
#         Counter[i] = Counter[i] + int(line[i])

# print(Counter)

# gamma = [0] * (len(Counter))
# epsilon = [0] * (len(Counter))
# for i in range(0, len(Counter)):
#     if(Counter[i] > len(report) / 2):
#         gamma[i] = '1'
#         epsilon[i] = '0'
#     else:
#         gamma[i] = '0'
#         epsilon[i] = '1'

# gammaValue = int(''.join(str(i) for i in gamma), 2)
# epsilonValue = int(''.join(str(i) for i in epsilon), 2)

# print('Gamma:', gamma, 'Val:', gammaValue)
# print('Epsilon:', epsilon, 'Val:', epsilonValue)

# result = gammaValue * epsilonValue

# print('Result:', result)
