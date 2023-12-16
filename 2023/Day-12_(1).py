from itertools import combinations

with open("testcase.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
result = 0  # a variable to store the result

def is_matching(pattern, contiguous_sizes): # given a pattern (without '?') and an array of contiguous sizes, checking if it aligns
    sizes_ind = 0   
    n = len(contiguous_sizes)
    length = 0  # stores the current length of consecutive '#'
    for char in pattern:
        if(char == '#'):
            length += 1
        else:
            if(length != 0):
                if(sizes_ind >= n): # if there are more '#', return false
                    return False
                if(length != contiguous_sizes[sizes_ind]):  # if it doesn't align with the array, return false
                    return False
                sizes_ind += 1
            length = 0
    
    if(length != 0):
        if(sizes_ind >= n):
            return False
        if(length != contiguous_sizes[sizes_ind]):
            return False
        sizes_ind += 1
        
    return sizes_ind == n   # atlast, check if we covered all contiguous blocks


def count_ways(pattern, contiguous_sizes):  # given a pattern and an array of contiguous sizes, return the number of possibilities
    ans = 0

    total_damages = sum(contiguous_sizes)   # total number of '#' according to the consecutive blocks size numbers
    pattern_damages = 0 # How many are already present in the pattern
    for char in pattern:
        if(char == '#'):
            pattern_damages += 1

    missing_damages = total_damages-pattern_damages # extra damages that must be added (by replacing '?' with '#')
    possibilities = []  # an array holding all the indices whose character is '?'

    for i, char in enumerate(pattern):  
        if(char == '?'):
            possibilities.append(i)

    # we need "missing_damages" of the '?' to be converted into '#'
    # so we will choose "missing_damages" number of '?' from all the available '?' and convert them into '#'
    # now we will check if this new pattern aligns with the sizes of consecutive blocks
    # if yes, we will update the counter
    # we will keep doing it for all combinations
            
    for comb in combinations(possibilities, missing_damages):
        for i in comb:
            pattern[i] = '#'

        if(is_matching(pattern, contiguous_sizes)):
            ans += 1

        for i in comb:
            pattern[i] = '?'

    return ans


for line in data:   # this is just converting the data in the format requested by the functions written above
    pattern, continguous_sizes = line.split(" ")
    pattern = list(pattern)
    continguous_sizes = [int(x) for x in continguous_sizes.split(",")]
    result += count_ways(pattern, continguous_sizes)


print(result)


    
        

    