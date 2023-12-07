import re

# In this variant, we will just change value of 'J' in the cards_value
# and we will make 'J' take the card which maximizes the power of hand

with open("input.txt") as file:
    data = file.read()

data = data.split("\n")
cards_pat = re.compile(r"^\w+")
bets_pat = re.compile(r"\d+$")


cards_value = {
    'J': 0,     # Notice value of 'J' is changed
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}

cards_count = [0]*13
cards_bets = []
weight_for_same_cards = 13**5

def hand_value(x):  # takes a [hand, bet] and returns an integer based on the strength of hand
    hand = x[0]
    val = 0
    count_j = 0

    for i in range(13):
        cards_count[i] = 0

    for card in hand:
        if(card == 'J'):    # if we encounter 'J', don't include it yet!
            count_j += 1
            continue
        cards_count[cards_value[card]] += 1

    max_count = max(cards_count)        # We will use the 'J's to increase the occurence of card which occurs most often
    max_count_ind = cards_count.index(max_count)
    cards_count[max_count_ind] += count_j

    # giving value for sameness of a card
    for count in cards_count:
        val += 13**count
    
    # We have to prioritize sameness of card before we compare individual cards
    val *= weight_for_same_cards

    # Now, let's give value to each card based on it's position in hand
    for i in range(5):
        val += cards_value[hand[4-i]]*(13**i)

    return val





    

for line in data:
    card = re.search(cards_pat, line).group()
    bet = int(re.search(bets_pat, line).group())
    cards_bets.append([card, bet])


sorted_list = sorted(cards_bets, key=hand_value)
res = 0


for i in range(len(sorted_list)):   # calculating the asked value
    res += (i+1)*sorted_list[i][1]

print(res)
