
with open("testcase.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
r = len(data)
c = len(data[0])

map = []
for line in data:
    map.append([int(x) for x in line])

curr_x, curr_y = 0, 0
cost = 0
seen = set()
seen.add((0, 0))
path = []
memoize = {}

def explore(curr_x, curr_y):
    global r, c, seen, map, path, memoize

    if((curr_x, curr_y) in memoize):
        return memoize[(curr_x, curr_y)]

    if((curr_x == r-1) and (curr_y == c-1)):
        memoize[(curr_x, curr_y)] = 0
        return 0
    
    mn = 1e20

    # checking left
    if((curr_y - 1 >= 0) and ((curr_x, curr_y-1) not in seen)):
        if(not ((len(path) >= 3) and (path[-1] == 'L') and (path[-2] == 'L') and (path[-3] == 'L'))):
            path.append('L')
            seen.add((curr_x, curr_y-1))
            mn = min(mn, map[curr_x][curr_y-1]+explore(curr_x, curr_y-1))
            seen.remove((curr_x, curr_y-1))
            path.pop()

    # checking right
    if((curr_y + 1 < c) and ((curr_x, curr_y+1) not in seen)):
        if(not ((len(path) >= 3) and (path[-1] == 'R') and (path[-2] == 'R') and (path[-3] == 'R'))):
            path.append('R')
            seen.add((curr_x, curr_y+1))
            mn = min(mn, map[curr_x][curr_y+1]+explore(curr_x, curr_y+1))
            seen.remove((curr_x, curr_y+1))
            path.pop()

    # checking up
    if((curr_x - 1 >= 0) and ((curr_x-1, curr_y) not in seen)):
        if(not ((len(path) >= 3) and (path[-1] == 'U') and (path[-2] == 'U') and (path[-3] == 'U'))):
            path.append('U')
            seen.add((curr_x-1, curr_y))
            mn = min(mn, map[curr_x-1][curr_y] + explore(curr_x-1, curr_y))
            seen.remove((curr_x-1, curr_y))
            path.pop()

    # checking down
    if((curr_x + 1  < r) and ((curr_x+1, curr_y) not in seen)):
        if(not ((len(path) >= 3) and (path[-1] == 'D') and (path[-2] == 'D') and (path[-3] == 'D'))):
            path.append('D')
            seen.add((curr_x+1, curr_y))
            mn = min(mn, map[curr_x+1][curr_y] + explore(curr_x+1, curr_y))
            seen.remove((curr_x+1, curr_y))
            path.pop()

    memoize[(curr_x, curr_y)] = mn
    return mn

    

print(explore(0, 0))
print(memoize)
