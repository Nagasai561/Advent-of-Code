import re
import math

with open("input.txt") as file:
    data = file.read()

num_pat = re.compile(r"\b\d+\b")    # pattern to match numbers
data = data.split("\n")     # splitting the data so that there are no newlines

times = [int(x.group()) for x in num_pat.finditer(data[0])]     # A list of all times
distances = [int(x.group()) for x in num_pat.finditer(data[1])] # A list of all distances

result = 1      # a variable to store our final result
n = len(times)  

# Suppose the distance is d and time is t
# We want the number of solutions to (t-x)*x > d
# The graph is inverted parabola and it is symmtric about (x = t/2) line
# As function is monotonic on the right half, we will use binary search to get largest x satisfying the condition
# As it it symmetric, we don't have to repeat it for left half
# As you keep getting these answers, mulitply it with result, to get the final answer

for i in range(n):
    time = times[i]
    dis = distances[i]
    
    start = math.ceil(time/2.0)
    left = start
    right = time
    while(left+1 < right):
        mid = (left+right)//2
        if((mid*(time-mid)) > dis):
            left = mid
        else:
            right = mid
    
    count_right_side = left-start+1
    
    if(time%2 == 0):
        result *= 2*count_right_side-1
    else:
        result *= 2*count_right_side

print(result)
