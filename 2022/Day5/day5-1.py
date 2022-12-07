#Advent of Code 2022 Day 5 - 1

with open('input.txt') as input:
    input = input.readlines()
    #input = [items.strip('\n') for items in input]

columns = []
for i in range(9):
    columns.append([])

for line in input:
    if line != '\n' and line[0:4] != 'move': #Get starting info
        i = 0
        for j in range(0, len(line), 4):
            if not line[j].isspace():
                columns[i].insert(0, line[j:j+3])
            i += 1
    elif line[0:4] == 'move': #Move crates
        for i in range(int(line[5])): #How many crates to move
            columns[int(line[17])-1].append(columns[int(line[12])-1].pop())
    else:
        print('Init', columns)

print('End of moves', columns)
topBoxes = []
for row in columns:
    if len(row) != 0:
        topBoxes.append(row.pop())
print('Code', topBoxes)