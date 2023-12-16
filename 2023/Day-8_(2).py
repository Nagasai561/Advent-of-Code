import itertools
import re
import math

# playing around with data, we will notice that upon following the directions as mentioned
# we will end up with paths which look like a --> b --> b --> b --> b
# where 'a' is word ending with 'A' and b is a word ending with 'Z'
# note that there is no other word ending with 'Z' between the intermediate path nodes
# And each intermediate path length is a multiple of length of "moves", so it will keep repeating in that pattern
# So, our idea is to figure out the length of cycle for each word ending with 'A' 
# and take lcm of all those numbers

with open("input.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
pat = re.compile(r"\w\w\w")

moves = data[0]
data = data[2:]
num_locations = len(data)

mapping = {}
ending_with_a = []
cycle_lengths = [] 

for line in data:
    locations = re.findall(pat, line)
    mapping[locations[0]] = [locations[1], locations[2]]

    if(locations[0][-1] == 'A'):
        ending_with_a.append(locations[0])


for start in ending_with_a:
    curr = start
    steps = 0
    for move in itertools.cycle(moves):
        if(move == 'L'):
            curr = mapping[curr][0]
        else:
            curr = mapping[curr][1]
        
        steps += 1

        if(curr[-1] == 'Z'):
            cycle_lengths.append(steps)
            break

print(math.lcm(*cycle_lengths))


    



    

    
    



