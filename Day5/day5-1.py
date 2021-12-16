#Advent of Code 2021 Day 5 - 1

# --- Day 5: Hydrothermal Venture ---

# You come across a field of hydrothermal vents on the ocean floor! These vents constantly produce large, opaque clouds, so it would be best to avoid them if possible.

# They tend to form in lines; the submarine helpfully produces a list of nearby lines of vents (your puzzle input) for you to review. For example:

# 0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2

# Each line of vents is given as a line segment in the format x1,y1 -> x2,y2 where x1,y1 are the coordinates of one end the line segment and x2,y2 are the coordinates of the other end. These line segments include the points at both ends. In other words:

#     An entry like 1,1 -> 1,3 covers points 1,1, 1,2, and 1,3.
#     An entry like 9,7 -> 7,7 covers points 9,7, 8,7, and 7,7.

# For now, only consider horizontal and vertical lines: lines where either x1 = x2 or y1 = y2.

# So, the horizontal and vertical lines from the above list would produce the following diagram:

# .......1..
# ..1....1..
# ..1....1..
# .......1..
# .112111211
# ..........
# ..........
# ..........
# ..........
# 222111....

# In this diagram, the top left corner is 0,0 and the bottom right corner is 9,9. Each position is shown as the number of lines which cover that point or . if no line covers that point. The top-left pair of 1s, for example, comes from 2,2 -> 2,1; the very bottom row is formed by the overlapping lines 0,9 -> 5,9 and 0,9 -> 2,9.

# To avoid the most dangerous areas, you need to determine the number of points where at least two lines overlap. In the above example, this is anywhere in the diagram with a 2 or larger - a total of 5 points.

# Consider only horizontal and vertical lines. At how many points do at least two lines overlap?














# class Bingo:

#     def __init__(self, numbers, boards) -> None:
#         self.drawPosition = int(0)
#         self.numbers = numbers
#         self.boards = boards
#         self.markers = [x[:] for x in boards]
#         self.lastSquare = [0] * 2
#         for line in self.markers:
#             for i in range(0, len(line)):
#                 line[i] = '0'

#         pass

#     def drawNumber(self):
#         if(self.drawPosition == len(self.numbers)):
#             return -1
#         number = self.numbers[self.drawPosition]
#         self.drawPosition += 1
#         return number

#     def markPosition(self, value):
#         for y in range(0, len(self.boards)):
#             for x in range(0, len(self.boards[y])):
#                 if(self.boards[y][x] == value):
#                     self.markers[y][x] = '1'

#     def checkBingo(self):
#         for y in range(0, len(self.markers)):
#             xCounter = 0
#             for x in range(0, len(self.markers[0])):
#                 if(self.markers[y][x] == '1'):
#                     xCounter += 1
#                 if(xCounter == 5):
#                     self.lastSquare = [x, y]
#                     return 'Bingo'
                    
#         for x in range(0, len(self.markers[0])):
#             for y in range(0, len(self.markers)):
#                 if(y % 5 == 0): yCounter = 0
#                 if(self.markers[y][x] == '1'):
#                     yCounter += 1
#                 if(yCounter == 5):
#                     self.lastSquare = [x, y]
#                     return 'Bingo'

#     # Check only one board
#     def getUnmarkedValue(self):
#         value = int(0)
#         board = int(self.lastSquare[1] / 5) # Round down
#         for y in range(board * 5, board * 5 + 5):
#             for x in range(0, len(self.markers[y])):
#                 if(self.markers[y][x] == '0'):
#                     value += int(self.boards[y][x])
#         return value


# #### Main ####

# with open('Input.txt') as input:
#     numbers = input.readline()
#     numbers = numbers.split(',')
#     numbers = [value.strip('\n') for value in numbers]
#     boards = input.readlines()
#     boards = [line.strip('\n') for line in boards]
#     boards = [line.split(' ') for line in boards]
#     for line in boards:
#         while(line.count('') > 0):
#             line.remove('')
#     boards[:] = [x for x in boards if x]

# # print(boards)
# # exit()
# game = Bingo(numbers, boards)

# while(True):
#     number = game.drawNumber()
#     if(number == -1):
#         break
#     game.markPosition(number)
#     if(game.checkBingo() == 'Bingo'):
#         print('Bingo')
#         break

# print('Last number:', number)
# print('Last square:', game.lastSquare)
# unmarkedValues = game.getUnmarkedValue()
# print('Unmarked values in winning board', unmarkedValues)
# result = unmarkedValues * int(number)
# print('Result:', result)
