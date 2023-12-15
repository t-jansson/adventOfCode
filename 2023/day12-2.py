#Advent of Code 2023 Day 12 - 2

import re

matches = set()

def solve(record, hashes, row):
    
    index = [i.start() for i in re.finditer("\?", row)]
    # for i in index:
    if len(index) == 0:
        if row.count("#") != hashes:
            return
        print(row)
        x = re.search(record, row)
        if x is not None:
            # print(row)
            matches.add(row)
        return
    if index[0] < len(row):
        newStr = row[:index[0]] + "#" + row[index[0]+1:]
        # print(newStr)
        solve(record, hashes, newStr)
        newStr = row[:index[0]] + "." + row[index[0]+1:]
        # print(newStr)
        solve(record, hashes, newStr)
    else:
        newStr = row[:index[0]] + "#"
        # print(newStr)
        solve(record, hashes, newStr)
        newStr = row[:index[0]] + "."
        # print(newStr)
        solve(record, hashes, newStr)
            


if __name__ == "__main__":

    with open('day12_input.txt') as input:
        data = input.readlines()
    data = [d.split() for d in data]
    rows = [d[0] for d in data]
    records = [d[1].split(",") for d in data]

    rows = [("?".join([row*5])) for row in rows]
    records = [record*5 for record in records]

    result = 0
    for row, record in zip(rows, records):
        print(row, record)
        index = 0
        sub = ""
        hashes = 0
        for i, rec in enumerate(record):
            rec = int(rec)
            hashes += rec
            sub += "[#]" * rec
            if i < len(record)-1:
                sub += "[.]+"
        solve(sub, hashes, row)
        result += len(matches)
        matches.clear()
    print(result)