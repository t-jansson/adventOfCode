#Advent of Code 2021 Day 4 - 1

class Bingo:

    def __init__(self, numbers, boards) -> None:
        self.drawPosition = int(0)
        self.numbers = numbers
        self.boards = boards
        self.markers = [x[:] for x in boards]
        self.lastSquare = [0] * 2
        for line in self.markers:
            for i in range(0, len(line)):
                line[i] = '0'

        pass

    def drawNumber(self):
        if(self.drawPosition == len(self.numbers)):
            return -1
        number = self.numbers[self.drawPosition]
        self.drawPosition += 1
        return number

    def markPosition(self, value):
        for y in range(0, len(self.boards)):
            for x in range(0, len(self.boards[y])):
                if(self.boards[y][x] == value):
                    self.markers[y][x] = '1'

    def checkBingo(self):
        for y in range(0, len(self.markers)):
            xCounter = 0
            for x in range(0, len(self.markers[0])):
                if(self.markers[y][x] == '1'):
                    xCounter += 1
                if(xCounter == 5):
                    self.lastSquare = [x, y]
                    return 'Bingo'
                    
        for x in range(0, len(self.markers[0])):
            for y in range(0, len(self.markers)):
                if(y % 5 == 0): yCounter = 0
                if(self.markers[y][x] == '1'):
                    yCounter += 1
                if(yCounter == 5):
                    self.lastSquare = [x, y]
                    return 'Bingo'

    # Check only one board
    def getUnmarkedValue(self):
        value = int(0)
        board = round(self.lastSquare[1] / 5)
        for y in range(board * 5, board * 5 + 5):
            for x in range(0, len(self.markers[y])):
                if(self.markers[y][x] == '0'):
                    value += int(self.boards[y][x])
        return value


#### Main ####

with open('Input.txt') as input:
    numbers = input.readline()
    numbers = numbers.split(',')
    numbers = [value.strip('\n') for value in numbers]
    boards = input.readlines()
    boards = [line.strip('\n') for line in boards]
    boards = [line.split(' ') for line in boards]
    for line in boards:
        while(line.count('') > 0):
            line.remove('')
    boards[:] = [x for x in boards if x]

# print(boards)
# exit()
game = Bingo(numbers, boards)

while(True):
    number = game.drawNumber()
    if(number == -1):
        break
    game.markPosition(number)
    if(game.checkBingo() == 'Bingo'):
        print('Bingo')
        break

print('Last number:', number)
#print('Last square:', game.lastSquare)
unmarkedValues = game.getUnmarkedValue()
print('Unmarked values in winning board', unmarkedValues)
result = unmarkedValues * int(number)
print('Result:', result)

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

