#Advent of Code 2023 Day 12 - 1

import re, itertools

if __name__ == "__main__":

    with open('day12_input.txt') as input:
        data = input.readlines()
    data = [d.split() for d in data]
    rows = [d[0] for d in data]
    records = [d[1].split(",") for d in data]

    result = 0
    for row, record in zip(rows, records):
        print(row, record)
        sub = ""
        for i, rec in enumerate(record):
            sub += "[?#]" *int(rec)
            if i < len(record)-1:
                sub += "[?.]+"
        print(sub)
        x = re.match(sub,row)
        print(x)
        #result += len(x)
        # searching = True
        # placements = []
        # while searching:
        #     if len(placements) > 0:
        #         for i, place in enumerate(placements):
        #             row = row[:place] + "." * int(record[i]) + row[place + int(record[i]):]
        #         placements = []
        #     index = 0
        #     for rec in record: #itertools.chain.from_iterable(itertools.repeat(record)): #
        #         rec = int(rec)
        #         sub = "[?#]" * rec 
        #         if len(row[index:]) > rec:
        #             sub += "[?.]"
        #         print(row[index:])
        #         x = re.search(sub, row[index:])
        #         if x == None:
        #             print("No match")
        #             searching = False
        #             break
        #         i, j = x.span()
        #         index += j
        #         placements.append(index-rec-1)
        #     if searching:
        #         result += 1
        #     print(placements)
