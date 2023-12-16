import itertools
import re

with open("input.txt") as file:
    data = file.read()

data = data.split("\n")
pat = re.compile(r"\w\w\w")

moves = data[0]

mp = {}

for i in range(2, len(data)):   # storing left and right in a dictionary
    letters = re.findall(pat, data[i])
    mp[letters[0]] = [letters[1], letters[2]]

current = "AAA"
move_count = 0

for move in itertools.cycle(moves): # keeping following instructions till you find 'ZZZ'
    move_count += 1
    if(move == 'L'):
        current = mp[current][0]
    else:
        current = mp[current][1]
    
    if(current == 'ZZZ'):
        break

print(move_count)

