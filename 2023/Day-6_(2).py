# We will use same strategy as before

import re
import math

with open("input.txt") as file:
    data = file.read()

num_pat = re.compile(r"\b\d+\b")    # pattern to match numbers
data = data.split("\n")     # splitting the data so that there are no newlines

times = int(''.join(num_pat.findall(data[0])))     
distances = int(''.join(num_pat.findall(data[1])))   

result = 1      # a variable to store our final result
 

# Suppose the distance is d and time is t
# We want the number of solutions to (t-x)*x > d
# The graph is inverted parabola and it is symmtric about (x = t/2) line
# As function is monotonic on the right half, we will use binary search to get largest x satisfying the condition
# As it it symmetric, we don't have to repeat it for left half
# As you keep getting these answers, mulitply it with result, to get the final answer


time = times
dis = distances

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
