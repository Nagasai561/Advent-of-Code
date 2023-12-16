# we will solve this problem by dynamic programming

# this function calculates the number of ways to changing '?', so that it aligns with nums
# note that here we are using 1 based indexing
def cal(pattern, nums):
    pattern_n = len(pattern)
    nums_n = len(nums)

    dp = [[0]*(pattern_n) for i in range(nums_n)]   # dp[i][j] represents the number of ways to make pattern[1:j+1] to align itself with nums[1:i+1] 
    
    for j in range(pattern_n):
        if(pattern[j] == '#'):
            break
        dp[0][j] = 1

    for i in range(1, nums_n):
        for j in range(1, pattern_n):
            if(pattern[j] != '#'):  # if pattern[j] isn't '#', then it might be not be a part of last block
                dp[i][j] += dp[i][j-1]
            
            if(j >= nums[i]):   # in this case, pattern[j] is a part of last block of '#'
                pos = True      
                for k in range(nums[i]):    # checking last whether last nums[j] characters can be made into '#'
                    if(pattern[j-k] == '.'):    # if not mark the flag as false
                        pos = False
                                                            # if the last block is possible
                        
                if((pos) and (j == nums[i]) and (i == 1)): # and we used up all the characters from pattern
                    dp[i][j] += 1                           # then add one to dp[i][j]

                if((pos) and (j > nums[i]) and (pattern[j-nums[i]] != '#')):    # and there are more characters towards left of the block
                    if((j-nums[i] == 1) and (i == 1)):  # if there is only one character and it is the first element ( != '#' )
                        dp[i][j] += 1   # then add one
                    if((j-nums[i] > 1)):    # if there are even more leftside
                        dp[i][j] += dp[i-1][j-nums[i]-1]    # then use the previous calculated value to make rest of it align
            
    return dp[nums_n-1][pattern_n-1]


with open("testcase.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
result = 0

for line in data:
    pattern, nums = line.split(" ")
    pattern = '.' + '?'.join([pattern for i in range(5)])
    nums = [0] + [int(x) for x in nums.split(',')]*5
    result += cal(pattern, nums)

print(result)