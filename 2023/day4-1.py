#Advent of Code 2023 Day 4 - 1

with open('day4_input.txt') as input:
    lines = input.readlines()

sum = 0
for line in lines:
    line = line.split(":")
    card = line[0]
    line = line[1].split("|")
    numbers = line[0].split()
    winningNumbers = line[1].split()

    cardValue = 0
    for number in numbers:
        try:
            if winningNumbers.index(number) >= 0:
                if cardValue == 0: cardValue = 1
                else: cardValue *= 2
        except ValueError:
            pass
    sum += cardValue

print(sum)