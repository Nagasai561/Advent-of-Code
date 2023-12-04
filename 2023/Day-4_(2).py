import re

with open("input.txt", 'r') as file:
    data = file.read()  

data = data.split("\n")
n = len(data)
count_cards = [1]*n # keeping track of how many of "card i" are present

num_pat = re.compile(r"\b\d+")  # searching for numbers

for i in range(n):
    grps = re.split(r"[:|]", data[i])

    winning_cards = []
    my_cards = []
    count = 0

    for num in num_pat.finditer(grps[1]):
        winning_cards.append(num.group())

    for num in num_pat.finditer(grps[2]):
        my_cards.append(num.group())

    for mine in my_cards:
        if(mine in winning_cards):
            count += 1

    for j in range(i+1, min(n, i+count+1)):
        count_cards[j] += count_cards[i]    # "Card i" contributes for one copy of "Card j"
                                            # As there are "count_cards[i]" "Card i"s, we add "count_cards[i]" instead of one
print(sum(count_cards))
