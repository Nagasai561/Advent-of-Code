with open("input.txt", 'r') as file:
    data = file.read()

data = [list(x) for x in data.split("\n")]  # creating a 2d array of characters
r = len(data)
c = len(data[0])


def move_up(x, y):     # moves the round rock at (x, y) as high as possible
    while((x-1 >= 0) and (data[x-1][y] == '.')):
        data[x][y], data[x-1][y] = data[x-1][y], data[x][y]
        x -= 1
    
for j in range(c):  # pushing all the round rocks to the top
    for i in range(r):
        if(data[i][j] == 'O'):
            move_up(i, j)

total_load = 0  # a variable to store the resulting total load

for i in range(r):
    num_round_rocks = 0 # counting how many round rocks are present in a single level
    for j in range(c):
        if(data[i][j] == 'O'):
            num_round_rocks += 1
    
    total_load += (c-i)*num_round_rocks # adding this level's contribution to total load

print(total_load)