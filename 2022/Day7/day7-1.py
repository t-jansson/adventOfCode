#Advent of Code 2022 Day 7 - 1

with open('input.txt') as input:
    commands = input.readlines()
    
folders = []
for command in commands:
    command = command.split()
    if command[0] == '$':
        if command[1] == 'ls':
            

print(folders)