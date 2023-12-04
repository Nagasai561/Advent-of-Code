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
    phrases = re.split(r";", line)                  # spliting the line at wherever we see ";"
    blue = 0
    red = 0
    green = 0
    for phrase in phrases:
        m = green_pat.search(phrase)
        if m:
            green_pre = int(num_pat.search(m.group()).group())      # getting number written beside green
            green = max(green, green_pre)           # Keeping track of the maximum number of green balls seen in this current game
        
        m = red_pat.search(phrase)
        if m:
            red_pre = int(num_pat.search(m.group()).group())
            red = max(red, red_pre)

        m= blue_pat.search(phrase)
        if m:
            blue_pre = int(num_pat.search(m.group()).group())
            blue = max(blue, blue_pre)

    result += blue*red*green

    


print(result)