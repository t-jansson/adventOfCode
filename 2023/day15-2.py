#Advent of Code 2023 Day 15 - 2

def calcHASH(hash):
    sum = 0
    for char in hash:
        sum += ord(char)
        sum = sum * 17
        sum = sum % 256
    return sum

boxes = [[] for i in range(256)]

if __name__ == "__main__":

    with open('day15_input.txt') as input:
        inputHASH = input.readline()
        inputHASH = inputHASH.strip()
        inputHASH = inputHASH.split(",")

    for hash in inputHASH:
        splitSign = "-" if hash.count("-") > 0 else "="
        label, focal = hash.split(splitSign)
        box = calcHASH(label)
        if splitSign == "=":
            labelExists = False
            for i in range(len(boxes[box])):
                if label == boxes[box][i][0]:
                    boxes[box][i][1] = focal
                    labelExists = True
            if not labelExists:
                boxes[box].append([label, focal])
        else:
            for i in range(len(boxes[box])):
                if label == boxes[box][i][0]:
                    boxes[box].remove(boxes[box][i])
                    break

    result = 0
    for i, box in enumerate(boxes):
        for j in range(len(box)):
            result += (i+1) * (j+1) * int(box[j][1])

    print("Resumt", result)