import copy

with open("input.txt", 'r') as file:
    data = file.read()

data = [list(x) for x in data.split("\n")]
r = len(data)
c = len(data[0])

def move(x, y, dir): # dir is the direction in which we want to move the rounded rocks
    while((0 <= x+dir[0] < r) and (0 <= y+dir[1] < c) and (data[x+dir[0]][y+dir[1]] == '.')):
        data[x][y], data[x+dir[0]][y+dir[1]] = data[x+dir[0]][y+dir[1]], data[x][y]
        x += dir[0]
        y += dir[1]

def cycle():
    # moving rocks to north
    for j in range(c):
        for i in range(r):
            if(data[i][j] == 'O'):
                move(i, j, [-1, 0])

    # moving rocks to west
    for i in range(r):
        for j in range(c):
            if(data[i][j] == 'O'):
                move(i, j, [0, -1])

    # moving rocks to south
    for i in range(r-1, -1, -1):
        for j in range(c):
            if(data[i][j] == 'O'):
                move(i, j, [1, 0])

    # moving rocks to east
    for j in range(c-1, -1, -1):
        for i in range(r):
            if(data[i][j] == 'O'):
                move(i, j, [0, 1])


list_all_config = []
list_all_config.append(copy.deepcopy(data))
last_distinct_iteration = 117   # this number is found through experiments
next_iteration = 96 # Again by experiments we note that after 118th iteration, the data looks exactly like the one at 96th index of "list_all_config" list

for i in range(last_distinct_iteration):
    cycle()
    list_all_config.append(copy.deepcopy(data))



cycles = 1000000000
last_config = list_all_config[96+(cycles-118)%(len(list_all_config)-next_iteration)]



total_load = 0  # a variable to store the resulting total load

for i in range(r):
    num_round_rocks = 0 # counting how many round rocks are present in a single level
    for j in range(c):
        if(last_config[i][j] == 'O'):
            num_round_rocks += 1
    
    total_load += (c-i)*num_round_rocks # adding this level's contribution to total load

print(total_load)