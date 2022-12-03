#Advent of Code 2021 Day 4 - 2

class Bingo:

    def __init__(self, numbers, boards) -> None:
        self.drawPosition = int(0)
        self.numbers = numbers
        self.boards = boards
        self.markers = [x[:] for x in boards]
        self.lastSquare = [0] * 2
        self.boardsWon =  [0] * int((len(self.boards) / 5))
        for line in self.markers:
            for i in range(0, len(line)):
                line[i] = 0

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
                    self.markers[y][x] = 1

    def checkBingo(self):
        for y in range(0, len(self.markers)):
            xCounter = 0
            for x in range(0, len(self.markers[0])):
                if(self.markers[y][x] == 1):
                    xCounter += 1
                if(xCounter == 5):
                    self.boardsWon[int(y/5)] = 1
                    if(self.checkLastBoard()):
                        self.lastSquare = [x, y]
                        return True
                    
        for x in range(0, len(self.markers[0])):
            for y in range(0, len(self.markers)):
                if(y % 5 == 0): yCounter = 0
                if(self.markers[y][x] == 1):
                    yCounter += 1
                if(yCounter == 5):
                    self.boardsWon[int(y/5)] = 1
                    if(self.checkLastBoard()):
                        self.lastSquare = [x, y]
                        return True
        return False

    def checkLastBoard(self):
        count = int(0)
        for value in self.boardsWon:
            count += value
        if(count == 100):
            return True
        else:
            return False

    # Check only one board
    def getUnmarkedValue(self):
        value = int(0)
        board = int(self.lastSquare[1] / 5) # Round down
        for y in range(board * 5, board * 5 + 5):
            for x in range(0, len(self.markers[y])):
                if(self.markers[y][x] == 0):
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
    if(game.checkBingo()):
        print('Bingo')
        break

print('Last number:', number)
print('Last square:', game.lastSquare)
unmarkedValues = game.getUnmarkedValue()
print('Unmarked values in winning board', unmarkedValues)
result = unmarkedValues * int(number)
print('Result:', result)
