# these represent what coordinates are connected by each character
connections = {
    '-': [(0, 1), (0, -1)],
    '|': [(1, 0), (-1, 0)],
    'J': [(-1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
    '7': [(0, -1), (1, 0)],
    'L': [(-1, 0), (0, 1)], 
    'S': []
}

with open("input.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
r = len(data)
c = len(data[0])

s_x, s_y = -1, -1   # x, y coordinates of 'S'

for i in range(r):
    for j in range(c):
        if(data[i][j] == 'S'):
            s_x = i
            s_y = j
            break
    if(s_x != -1):
        break

for i in [-1, 1]:   # trying to deduce the connection of 'S' from it's surrounding pipes
    if(0 <= s_x + i < r):
        if((data[s_x+i][s_y] in connections) and ((-i, 0) in connections[data[s_x+i][s_y]])):
            connections['S'].append((i, 0))

for j in [-1, 1]:
    if(0 <= s_y + i < c):
        if((data[s_x][s_y+j] in connections) and ((0, -j) in connections[data[s_x][s_y+j]])):
            connections['S'].append((0, j))

path = set()    # a set to store coordinates of path
path.add((s_x, s_y))    # initializing it with starting location
curr_x = s_x
curr_y = s_y


while True: # looping indefinitely
    for i, j in connections[data[curr_x][curr_y]]:  # exploring all connection at current coordinate
        if((0 <= curr_x + i < r) and (0 <= curr_y + j < c)):    # if it is within bounds
            if((data[curr_x+i][curr_y+j] in connections) and ((-i, -j) in connections[data[curr_x+i][curr_y+j]])):  # neighbour is also connected to current position
                if((curr_x+i, curr_y+j) not in path):   # the node isn't already present in the path, then change it to be the current position
                    curr_x += i
                    curr_y += j
                    break

    node = (curr_x, curr_y)
    if(node in path):   # if we encountered the node in the path before, we exit the loop
        break
    path.add(node)  # otherwise, we add the node to the path

# we will determine whether a point lies inside the current path by "ray-casting" algorithm
# the ray which we use is y = -x. 
# Note that we might run into pointy corners, in which this ray doesn't give correct result
# So, whenever we encounter a pointy corner, we will double count it!
    
num_inside = 0  # number of tiles insider the loop

for i in range(r):
    for j in range(c):
        if((i, j) not in path): # drawing a ray from (i, j) with slope -1
            count_intersections = 0    
            x = i
            y = j
            while((x+1 < r) and (y+1 < c)):
                x += 1
                y += 1
                if((x, y) in path):
                    count_intersections += 1
                    if((data[x][y] == '7') or (data[x][y] == 'L')):   # if it's a pointy corner, increase it by one more
                        count_intersections += 1    
            if(count_intersections%2 == 1): # if the number of intersections in odd, then it is interior tile, so increase "num_inside" by one.
                num_inside += 1


print(num_inside)

