import re

with open("input.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
num_pattern = re.compile(r"\b\d+")  # find the numbers 
result = 0

for line in data:
    grps = re.split(r"[:|]", line)
    points = -1
    winning_cards = []  # store all the winning cards here
    my_cards = []       # store all the cards I have 

    for num in num_pattern.finditer(grps[1]):
        winning_cards.append(num.group())

    for num in num_pattern.finditer(grps[2]):
        my_cards.append(num.group())
    
    for mine in my_cards:   # if my card is present in winning cards, increment the points
        if(mine in winning_cards):
            points += 1
    
    if(points != -1):
        result += 2**points
    
print(result)

