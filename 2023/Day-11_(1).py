with open("input.txt", 'r') as file:
    data = file.read()  

data = data.split("\n") # getting the input file

galaxies = []   # array to store coordinates of all galaxies
r = len(data)   # number of rows
c = len(data[0])   # number of columns


for i in range(r):  
    for j in range(c):
        if(data[i][j] == '#'):
            galaxies.append([i, j])

dis_sum = 0 # we are storing all the distances in this variable

# First let's calculate the sum of distances without considering the expansion
for i in range(len(galaxies)):
    for j in range(i+1, len(galaxies)):
        dis_sum += abs(galaxies[i][0]-galaxies[j][0]) + abs(galaxies[i][1]-galaxies[j][1])

# we will store prefix row and col sum
# These will store number of galaxies till ith row/col
prefix_row_sum = [0]*r
prefix_col_sum = [0]*c

temp = 0

for i in range(r):
    cnt = 0
    for j in range(c):
        if(data[i][j] == '#'):
            cnt += 1
    temp += cnt
    prefix_row_sum[i] = temp

temp = 0

for j in range(c):
    cnt = 0
    for i in range(r):
        if(data[i][j] == '#'):
            cnt += 1
    temp += cnt
    prefix_col_sum[j] = temp

# Consider a row, which has no galaxies
# Consider all the galaxies towards left of it and right of it
# Due to expansion of this row, the distance between on galaxy on left side and another galaxy on right side
# increases by 1
# in total the increase will be (no of galaxies on left side * no of galaxies on right side)


for i in range(1, r-1):
    if(prefix_row_sum[i] == prefix_row_sum[i-1]):
        dis_sum += prefix_row_sum[i]*(prefix_row_sum[r-1]-prefix_row_sum[i])

for j in range(1, c-1):
    if(prefix_col_sum[j] == prefix_col_sum[j-1]):
        dis_sum += prefix_col_sum[j]*(prefix_col_sum[c-1]-prefix_col_sum[j])

print(dis_sum)
