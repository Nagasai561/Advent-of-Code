# a map that outputs the number when given it's spelling
word_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

# loading the file
with open("input.txt", 'r') as file:
    text = file.read()

# storing the result in a variable
result = 0

for line in text.split("\n"):
    digits_seen = []
    n = len(line)
    for i in range(n):
        if(line[i].isdigit()):    # checking if ith character is a digit or not
            digits_seen.append(int(line[i]))    # if yes put it in the "digits_seen" list
        for spel in word_to_num.keys():     # iterating over all spellings of digits
            if(line[i:min(i+len(spel), n)] == spel):    # checking whether the spelling of digit can start from this position
                digits_seen.append(word_to_num[spel])   # If yes, put it in the "digits_seen" list
    
    result += digits_seen[0]*10 + digits_seen[-1]   # get the last and first digits, make a two digit number out of it and add it to "result"

print(result)
