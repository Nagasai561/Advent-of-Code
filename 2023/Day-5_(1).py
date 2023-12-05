import re

with open("input.txt") as file:
    data = file.read()

data = re.split(r"\n+", data)   # split the data conviniently so that no newlines are present

num_pat = re.compile(r"\b\d+")  # matches numbers
map_pat = re.compile(r"map")    # mathces the word "map"

maps_list = []      # A list to store all seeds numbers
seeds_list = []     # A list to store all maps. We will store map as collection of list
# Each list is of form [starting, ending, diff]
# This means every number x, such that (starting <= x <= ending) will be changed by (diff)


for num in num_pat.finditer(data[0]):   # getting seeds
    seeds_list.append(int(num.group()))

for i in range(1, len(data)):
    if(map_pat.search(data[i]) != None):    # If I encounter a word "map", it means it's time to start a new map
        maps_list.append([])
    else:
        numbers = [int(x.group()) for x in num_pat.finditer(data[i])]   # getting the three numbers
        starting = numbers[1]
        ending = numbers[1]+numbers[2]-1
        diff = numbers[0]-numbers[1]
        maps_list[-1].append([starting, ending, diff])      # Adding a new list to our current map

location_list = []      # A list to store location of each seed

for seed in seeds_list: # Iterate over seeds
    num = seed
    for mp in maps_list:    # Iterate over maps
        for rang in mp:     # If we can find the seed in the map, then change it according to the value of diff
            if((num >= rang[0]) and (num <= rang[1])):  # If we can't find it, then it means it gets mapped to itself, so no need to change it
                num += rang[2]
                break
    location_list.append(num)

print(min(location_list))






