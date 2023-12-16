import re

def extrapolate(xs):    # function to extrapolate the given sequence
    if(len(xs) == 1):   # if length of list is 0. Then return 0
        return 0
    
    diff_xs = []         # we are making a difference array now
    for i in range(len(xs)-1):
        diff_xs.append(xs[i+1]-xs[i])
    
    diff_extrapolate = extrapolate(diff_xs)   # Find extrapolated value of this new difference array

    return xs[-1]+diff_extrapolate   # Use the extrapolated value of difference to get extrapolated value of original sequence

# patten to match negative/postive integers separated by spaces
num_pat = re.compile(r"-?\d+")

# reading the data
with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
res = 0     # a variable to hold the required answer

for line in data:
    nums = [int(x.group()) for x in re.finditer(num_pat, line)] # turning the readline into list of ints
    res += extrapolate(nums)    # adding the extrapolate to the result variable

print(res)

