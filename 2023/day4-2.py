#Advent of Code 2023 Day 4 - 2

with open('day4_input.txt') as input:
    lines = input.readlines()

wins = [1 for x in range(1,len(lines)+1)]

index = 0
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
                cardValue += 1
        except ValueError:
            pass
    
    for i in range(index+1, index+1+cardValue):
        wins[i] += wins[index]

    index += 1

sum = 0
for win in wins:
    sum += win

print(sum)