#Advent of Code 2021 Day 4 - 1

class Bingo:

    def __init__(self, numbers, boards) -> None:
        self.drawPosition = int(0)
        self.numbers = numbers.split(',')
        self.boards = boards
        self.markers = [x[:] for x in boards]
        for line in self.markers:
            for i in range(0, len(line)):
                line[i] = '0'

        pass

    def drawNumber(self):
        number = self.numbers[self.drawPosition]
        self.drawPosition += 1
        return number

    def markPosition(self, value):
        


with open('Input.txt') as input:
    numbers = input.readline()
    boards = input.readlines()
    boards = [line.strip('\n') for line in boards]
    # boards = [line.replace(' ', '') for line in boards]
    boards = [line.split(' ') for line in boards]
    for line in boards:
        while(line.count('') > 0):
            line.remove('')

game = Bingo(numbers, boards)

print(game.drawNumber())
print(game.drawNumber())
print(game.drawNumber())
print(game.drawNumber())
print(game.drawNumber())

# oxygenData = [line.strip('\n') for line in report]
# for i in range(0, len(oxygenData[0])):
#     if(len(oxygenData) == 1):
#         break
#     counter = int(0)
#     length = len(oxygenData)
#     # print('Length:', length)
#     for data in oxygenData:
#         if(data[i] == '1'):
#             counter += 1
#     # print('Counter:', counter)
#     if(counter >= length / 2):
#         mostCommon = '1'
#     else:
#         mostCommon = '0'
#     # print('MostCommon:', mostCommon)
#     newData = []
#     for data in oxygenData:
#         if(data[i] == mostCommon):
#             # print(i, data)
#             newData.append(data)
#     oxygenData = newData
# oxygenValue = int(''.join(str(i) for i in oxygenData), 2)
# print(oxygenData, oxygenValue)

# co2Data = [line.strip('\n') for line in report]
# for i in range(0, len(co2Data[0])):
#     if(len(co2Data) == 1):
#         break
#     counter = int(0)
#     length = len(co2Data)
#     # print('Length:', length)
#     for data in co2Data:
#         if(data[i] == '1'):
#             counter += 1
#     # print('Counter:', counter)
#     if(counter >= length / 2):
#         mostCommon = '0'
#     else:
#         mostCommon = '1'
#     # print('MostCommon:', mostCommon)
#     newData = []
#     for data in co2Data:
#         if(data[i] == mostCommon):
#             # print(i, data)
#             newData.append(data)
#     co2Data = newData
# co2Value = int(''.join(str(i) for i in co2Data), 2)
# print(co2Data, co2Value)

# print('Result:', oxygenValue * co2Value)

