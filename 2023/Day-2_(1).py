import re

# loading file
with open("input.txt", "r") as file:
    text = file.read()


num_pat = re.compile(r"\d+")    # matches all numbers
green_pat = re.compile(r"\d+ green")    # matches "12 green"
red_pat = re.compile(r"\d+ red")        # matches "4 red"
blue_pat = re.compile(r"\d+ blue")      # matches "15 blue"

blue_max = 14
green_max = 13
red_max = 12
result = 0

for line in text.split("\n"):
    game_id = int(num_pat.search(line).group())
    phrases = re.split(r";", line)                  # spliting the line at wherever we see ";"
    wrong = False
    for phrase in phrases:
        m = green_pat.search(phrase)
        if m and (int(num_pat.search(m.group()).group()) > green_max):  # if green exists and it's number is greater than green_max
            wrong = True
        
        m = red_pat.search(phrase)
        if m and (int(num_pat.search(m.group()).group()) > red_max):    # same thing for red
            wrong = True

        m= blue_pat.search(phrase)
        if m and (int(num_pat.search(m.group()).group()) > blue_max):   # same thing for blue
            wrong = True
    
    if(not wrong):
        result += game_id


print(result)