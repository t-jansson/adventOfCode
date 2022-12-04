#Advent of Code 2022 Day 2 - 2

with open('input.txt') as input:
    input = input.readlines()

score = 0

for hand in input:
    hand = hand.split()
    if(hand[1] == 'X'): #Lose
        if(hand[0] == 'A'): #Elf Rock
            score = score + 3 #Me Scissor
        elif(hand[0] == 'B'): #Elf Paper
            score = score + 1 #Me Rock
        else: #Elf Scissor
            score = score + 2 #Me Paper
    elif(hand[1] == 'Y'):  #Draw
        score = score + 3
        if(hand[0] == 'A'): #Elf Rock
            score = score + 1 #Me Rock
        elif(hand[0] == 'B'): #Elf Paper
            score = score + 2 #Me Paper
        else: #Elf Scissor
            score = score + 3 #Me Scissor
    else: #Win
        score = score + 6
        if(hand[0] == 'A'): #Elf Rock
            score = score + 2 #Me Paper 
        elif(hand[0] == 'B'): #Elf Paper
            score = score + 3 #Me Scissor
        else: #Elf Scissor
            score = score + 1 #Me Rock

print(score)