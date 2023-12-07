import re


with open("input.txt") as file:
    data = file.read()

data = data.split("\n")
cards_pat = re.compile(r"^\w+")
bets_pat = re.compile(r"\d+$")

# we are giving each card a value from 0 to 12
# why? Because we are about to use Base-13 system to compare hands!
cards_value = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
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

    for i in range(13):
        cards_count[i] = 0

    for card in hand:
        cards_count[cards_value[card]] += 1

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
