#Advent of Code 2023 Day 1 - 2

numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

with open('day1_input.txt') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    firstDigit = [None, None]
    lastDigit = [None, None]
    # print(line)
    for i in range(0, len(numbers)):
        number = numbers[i]
        start = 0
        while(len(number) < len(line) - start):
            index = line.find(number, start)
            if index > -1: 
                if(i < 9):
                    number = numbers[i+9]
                start = index + 1
                # print(number, ":", index)
                if firstDigit[1] == None:
                    firstDigit = number, index
                elif firstDigit[1] > index:
                    firstDigit = number, index
                if lastDigit[1] == None:
                    lastDigit = number, index
                elif lastDigit[1] < index:
                    lastDigit = number, index
                number = numbers[i]
            else:
                break

    # print(firstDigit[0] + lastDigit[0])

    lineDigit = int(firstDigit[0] + lastDigit[0])
        
    sum += lineDigit

print(sum)
