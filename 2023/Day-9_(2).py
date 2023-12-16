import re

# same recursive code as before with little modifications here and there
def extrapolate_backward(xs):
    if(len(xs) == 1):
        return 0
    
    diff_xs = []
    for i in range(len(xs)-1):
        diff_xs.append(xs[i+1]-xs[i])
    
    diff_extrapolate = extrapolate_backward(diff_xs)

    return xs[0]-diff_extrapolate   # this is the key difference

with open("input.txt", "r") as file:
    data = file.read()

data = data.split("\n")
num_pat = re.compile(r"-?\d+")
res = 0

for line in data:
    nums = [int(x.group()) for x in re.finditer(num_pat, line)]
    res += extrapolate_backward(nums)

print(res)

