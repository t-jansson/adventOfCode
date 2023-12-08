#Advent of Code 2023 Day 5 - 2 not working

import threading, os

MINLOCATIONS = [0,0,0,0,0,0,0,0,0,0]

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
        if int(data[1]) <= input and input <= int(data[1]) + int(data[2]):
            output = int(data[0]) + (input - int(data[1]))
            break
    if output == 0: return input
    return output

def calcLocation():
    minLocation = 0
    start = int(seeds[int(threading.current_thread().name)*2])
    stop = int(seeds[int(threading.current_thread().name)*2]) + int(seeds[int(threading.current_thread().name)*2+1])
    for y in range(start, stop): #Tar för lång tid...
        # print(y)
        #seed = int(seed)
        soil = calc(y, seed_to_soil)
        fertilizer = calc(soil, soil_to_fertilizer)
        water = calc(fertilizer, fertilizer_to_water)
        light = calc(water, water_to_light)
        temperature = calc(light, light_to_temperature)
        humidity = calc(temperature, temperature_to_humidity)
        location = calc(humidity, humidity_to_location)
        # print(seed, location)
        if minLocation == 0 or location < minLocation:
            minLocation = location
    print("Thread", threading.current_thread().name, "done:", minLocation)        
    MINLOCATIONS[int(threading.current_thread().name)] = minLocation

if __name__ == "__main__":

    with open('input.txt') as input:
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


    t0 = threading.Thread(target=calcLocation, name="0")
    t1 = threading.Thread(target=calcLocation, name="1")
    t2 = threading.Thread(target=calcLocation, name="2")
    t3 = threading.Thread(target=calcLocation, name="3")
    t4 = threading.Thread(target=calcLocation, name="4")
    t5 = threading.Thread(target=calcLocation, name="5")
    t6 = threading.Thread(target=calcLocation, name="6")
    t7 = threading.Thread(target=calcLocation, name="7")
    t8 = threading.Thread(target=calcLocation, name="8")
    t9 = threading.Thread(target=calcLocation, name="9")

    t0.start()
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()

    t0.join()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()

    print("Min?", min(MINLOCATIONS))
    print("the end")