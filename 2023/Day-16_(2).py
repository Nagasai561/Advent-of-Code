# We are doing same thing as before
# we are making initial_ray to take all the possible orientations and getting it's answer
# and printing out the maximal answer

import time

 
class RAY:
    def __init__(self, x, y, v_x, v_y):
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y


with open("input.txt", 'r') as file:
    data = file.read()

data = data.split("\n")
r = len(data)
c = len(data[0])

def explore(initial_ray):
    rays_passed = []    # a list which says what oriented rays have passed through a certain coordinate
    energized = []      # a list which says which coordinates have been energized

    for i in range(r):
        rays_passed.append([])
        energized.append([])
        for j in range(c):
            rays_passed[-1].append([])
            energized[-1].append(False)

    rays = {initial_ray}    # a set which contains all the rays currently moving


    while rays:
        to_be_removed = []  # a list to store all the rays which must be removed after this turn (due to going out of board)
        to_be_added = []    # a list to store new rays to be added
        for ray in rays:    # for each ray that is currently present 
            if((0 <= ray.x + ray.v_x < r) and (0 <= ray.y + ray.v_y < c)):  # if the next cell is in valid bounds
                ray.x += ray.v_x
                ray.y += ray.v_y
                char = data[ray.x][ray.y]

                if(char == '\\'):   # if we encounter "\", then we have to change velocity direction and add this new ray to rays_passed[ray.x][ray.y]
                    ray.v_x, ray.v_y = ray.v_y, ray.v_x # But this type of ray has already passed through this coordinate, then we will delete this ray
                    if([ray.v_x, ray.v_y] in rays_passed[ray.x][ray.y]):
                        to_be_removed.append(ray)
                    else:
                        rays_passed[ray.x][ray.y].append([ray.v_x, ray.v_y])

                elif(char == '/'):  # Same thing as above
                    ray.v_x, ray.v_y = -ray.v_y, -ray.v_x
                    if([ray.v_x, ray.v_y] in rays_passed[ray.x][ray.y]):
                        to_be_removed.append(ray)
                    else:
                        rays_passed[ray.x][ray.y].append([ray.v_x, ray.v_y])

                elif(char == '-'):  # this is slightly trickier case
                    if(ray.v_y == 0):   # Then, the ray will split
                        to_be_removed.append(ray)   # remove the ray and put two new rays
                        right_ray = RAY(ray.x, ray.y, 0, 1)
                        left_ray = RAY(ray.x, ray.y, 0, -1)
                        to_be_added.append(right_ray)
                        to_be_added.append(left_ray)
                        if([left_ray.v_x, left_ray.v_y] in rays_passed[left_ray.x][left_ray.y]):    # did a ray of type left_ray already passed through this coordinates?
                            to_be_removed.append(left_ray)          # if yes, then we don't have to include this ray, so remove it
                        else:
                            rays_passed[left_ray.x][left_ray.y].append([left_ray.v_x, left_ray.v_y])    # otherwise, mark that this type of ray has gone through this coordinate
                        
                        if([right_ray.v_x, right_ray.v_y] in rays_passed[right_ray.x][right_ray.y]):    # same thing for right_ray
                            to_be_removed.append(right_ray)
                        else:
                            rays_passed[right_ray.x][right_ray.y].append([right_ray.v_x, right_ray.v_y])

                    else:    # Then, ray doesn't split, just goes as if nothing special happened
                        if([ray.v_x, ray.v_y] in rays_passed[ray.x][ray.y]):    
                            to_be_removed.append(ray)
                        else:
                            rays_passed[ray.x][ray.y].append([ray.v_x, ray.v_y])

                elif(char == '|'):  # Same thing as above
                    if(ray.v_x == 0):
                        to_be_removed.append(ray)
                        down_ray = RAY(ray.x, ray.y, 1, 0)
                        up_ray = RAY(ray.x, ray.y, -1, 0)
                        to_be_added.append(down_ray)
                        to_be_added.append(up_ray)
                        if([down_ray.v_x, down_ray.v_y] in rays_passed[down_ray.x][down_ray.y]):
                            to_be_removed.append(down_ray)
                        else:
                            rays_passed[down_ray.x][down_ray.y].append([down_ray.v_x, down_ray.v_y])
                        
                        if([up_ray.v_x, up_ray.v_y] in rays_passed[up_ray.x][up_ray.y]):
                            to_be_removed.append(up_ray)
                        else:
                            rays_passed[up_ray.x][up_ray.y].append([up_ray.v_x, up_ray.v_y])
                    else:
                        if([ray.v_x, ray.v_y] in rays_passed[ray.x][ray.y]):
                            to_be_removed.append(ray)
                        else:
                            rays_passed[ray.x][ray.y].append([ray.v_x, ray.v_y])
                
                energized[ray.x][ray.y] = True
            else:   # if not in valid bounds, then remove that ray 
                to_be_removed.append(ray)

        for ray in to_be_added: # add all the new rays to our list  
            rays.add(ray)
        for ray in to_be_removed:   # remove all the rays which have gone out of board
            if(ray in rays):
                rays.remove(ray)

        

    result = 0  # counting the number of energized coordinates
    for i in range(r):
        for j in range(c):
            if(energized[i][j]):
                result += 1

    return result

mx = 0 # storing the maximal answer encountered so far

for i in range(r):
    initial_ray = RAY(i, -1, 0, 1)
    mx = max(mx, explore(initial_ray))

    initial_ray = RAY(i, r, 0, -1)
    mx = max(mx, explore(initial_ray))



for j in range(c):
    initial_ray = RAY(-1, j, 1, 0)
    mx = max(mx, explore(initial_ray))

    initial_ray = RAY(c, j, -1, 0)
    mx = max(mx, explore(initial_ray))

print(mx)
