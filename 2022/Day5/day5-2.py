#Advent of Code 2022 Day 5 - 2

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
                columns[i].insert(0, line[j+1:j+2])
            i += 1

    elif line[0:4] == 'move': #Move crates
        moves = line.split()
        boxesToMove = columns[int(moves[3])-1][-int(moves[1]):]
        del columns[int(moves[3])-1][-int(moves[1]):]
        columns[int(moves[5])-1].extend(boxesToMove)

    else:
        print('Init', columns, '\n')

print('End of moves', columns, '\n')
topBoxes = []
for row in columns:
    if len(row) != 0:
        topBoxes.append(row.pop())
print('Code:', ''.join(topBoxes))