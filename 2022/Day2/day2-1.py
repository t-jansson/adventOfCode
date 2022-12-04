#Advent of Code 2022 Day 2 - 1

with open('input.txt') as input:
    input = input.readlines()

score = 0

for hand in input:
    hand = hand.split()
    if(hand[1] == 'X'): #Rock
        score = score + 1
        if(hand[0] == 'A'): #Draw
            score = score + 3
        elif(hand[0] == 'C'):
            score = score + 6
    elif(hand[1] == 'Y'):  #Paper
        score = score + 2
        if(hand[0] == 'B'): #Draw
            score = score + 3
        elif(hand[0] == 'A'):
            score = score + 6
    else: #Scissor
        score = score + 3
        if(hand[0] == 'C'): #Draw
            score = score + 3
        elif(hand[0] == 'B'):
            score = score + 6

print(score)