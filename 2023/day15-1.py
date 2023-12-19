#Advent of Code 2023 Day 15 - 1

if __name__ == "__main__":

    with open('day15_input.txt') as input:
        inputHASH = input.readline()
        inputHASH = inputHASH.strip()
        inputHASH = inputHASH.split(",")

    result = 0
    for hash in inputHASH:
        sum = 0
        for char in hash:
            sum += ord(char)
            sum = sum * 17
            sum = sum % 256
        result += sum
    print("Resumt", result)