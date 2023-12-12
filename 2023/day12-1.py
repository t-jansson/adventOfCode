#Advent of Code 2023 Day 12 - 1

import re

if __name__ == "__main__":

    with open('day12_input.txt') as input:
        data = input.readlines()
    data = [d.split() for d in data]
    rows = [d[0] for d in data]
    records = [d[1].split(",") for d in data]

    for row, record in zip(rows, records):
        print(row, record)
        index = 0
        for rec in record:
            rec = int(rec)
            sub = "[?#]" * rec + "[?.]"
            print(row[index:])
            x = re.search(sub, row[index:])
            if x == None:
                print("No match")
                break
            i, j = x.span()
            index += j
            print(i,j)