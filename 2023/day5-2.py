#Advent of Code 2023 Day 5 - 1

def getInfo(lines, index):
    data = []
    for x, line in enumerate(lines):
        if x < index: continue
        index = x
        if(line[0].isdigit()):
            data.append(line.split())
        else:
            index += 2
            break
    return data, index

def calc(input, dataList):
    output = 0
    for data in dataList:
        sourceMin = int(data[1])
        souceMax = int(data[1]) + int(data[2])
        
        if sourceMin <= input and input <= souceMax:
            output = int(data[0]) + (input - sourceMin)
            break
    if output == 0: output = input
    return output


with open('day5_input.txt') as input:
    lines = input.readlines()

seeds = lines[0].split(":")[1].split()

index = 3
seed_to_soil, index = getInfo(lines, index)
soil_to_fertilizer, index = getInfo(lines, index)
fertilizer_to_water, index = getInfo(lines, index)
water_to_light, index = getInfo(lines, index)
light_to_temperature, index = getInfo(lines, index)
temperature_to_humidity, index = getInfo(lines, index)
humidity_to_location, index = getInfo(lines, index)

locations = []
for seed in seeds:
    # print(seed)
    seed = int(seed)
    soil = calc(seed, seed_to_soil)
    fertilizer = calc(soil, soil_to_fertilizer)
    water = calc(fertilizer, fertilizer_to_water)
    light = calc(water, water_to_light)
    temperature = calc(light, light_to_temperature)
    humidity = calc(temperature, temperature_to_humidity)
    location = calc(humidity, humidity_to_location)
    # print(seed, location)
    locations.append(location)

print(min(locations))