import re

# After trying this problem for sometime, we can clearly see that it takes too much time if we solve it
# as we did in the previous part. According to my experiments, it will take more 2 hours to get it done on my laptop
# So, we need to figure out a new strategy. 
# Instead of working with one seed value at a time, we will work with ranges of seed values
# We will track how these ranges change on each mapping.
# At the end we will just report the minimum of ranges we have been left with

with open("input.txt") as file:
    data = file.read()

data = re.split(r"\n+", data)   # split the data conviniently so that no newlines are present

num_pat = re.compile(r"\b\d+")  # matches numbers
map_pat = re.compile(r"map")    # mathces the word "map"

range_list = []     # store our seed ranges in the collection of [start, end] lists
modifed_list = []      # In this we store our modified ranges after mapping

for i, x in enumerate(num_pat.finditer(data[0])):   # getting the seed ranges
    if(i%2 == 0):
        range_list.append([int(x.group())])
    else:
        left = range_list[-1][0]
        length = int(x.group())
        right = left+length-1
        range_list[-1].append(right) 

for i in range(1, len(data)):
    if(map_pat.search(data[i]) != None):    # If we see a word "map", it means we are done with previous mapping
        for j in range(len(range_list)):    # So, we will transfer over the non-mapped ranges from "range_list" to "modified_list"
            if(range_list[j] == [-1, -1]):  
                continue
            modified_list.append(range_list[j])
        range_list = modified_list
        modified_list = []
    else:
        numbers = [int(x.group()) for x in num_pat.finditer(data[i])]   # getting the three numbers from the input
        map_left = numbers[1]
        map_len = numbers[2]
        map_right = map_left+map_len-1
        map_diff = numbers[0]-numbers[1]        # What is the change due to this mapping
        for j in range(len(range_list)):
            range_left = range_list[j][0]
            range_right = range_list[j][1]

            if((map_left <= range_left) and (map_right >= range_right)):    # if range_list[j] is a part of current mapping range
                modified_list.append([range_left+map_diff, range_right+map_diff])
                range_list[j] = [-1,-1]
            elif((map_left > range_left) and (map_right < range_right)):    # if mapping range is a part of range_list[j]
                modified_list.append([map_left+map_diff, map_right+map_diff])
                range_list[j] = [range_left, map_left-1]
                range_list.append([map_right+1, range_right])
            elif((range_left <= map_left) and (map_left <= range_right)):   # they overlap on right side
                modified_list.append([map_left+map_diff, range_right+map_diff])
                range_list[j] = [range_left, map_left-1]
            elif((map_right >= range_left) and (map_right <= range_right)): # they overlap on left side
                modified_list.append([range_left+map_diff, map_right+map_diff])
                range_list[j] = [map_right+1, range_right]

            # if they don't overlap at all, then do nothing


for j in range(len(range_list)):    # Transfer over all the unmapped ranges from range_list to modified_list
    if(range_list[j] == [-1, -1]):
        continue
    modified_list.append(range_list[j])
    range_list = modified_list

mn = 1e20
for x in range_list:        # Getting the minimum of all elements present in range_list
    mn = min(x[0], mn)

print(mn)

