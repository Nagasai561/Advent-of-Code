import re

with open("input.txt", 'r') as file:
    raw_data = file.read()

raw_data = re.split(r"\n\n", raw_data)  # splitting each piece

data = []
for piece in raw_data:  # formatting each piece into lines
    temp = []
    for line in piece.split("\n"):
        temp.append(line)
    data.append(temp)

# check if the given piece has vertical reflection
# if it has vertical reflection, return the number of columns that are getting reflected
# otherwise return -1
def vertical_reflection(piece): 
    c = len(piece[0])
    r = len(piece)

    for line in range(0, c-1):
        pos = True
        for k in range(min(line+1, c-1-line)):
            for i in range(r):
                if(piece[i][line-k] != piece[i][line+1+k]):
                    pos = False
                    break
            
            if(not pos):
                break
        
        if(pos):
            return line+1
        
    return -1

# check if the given piece has horizontal reflection
# if it has horizontal reflection, return the number of rows that are getting reflected
# otherwise return -1
def horizontal_reflection(piece):
    c = len(piece[0])
    r = len(piece)

    for line in range(0, r-1):
        pos = True
        for k in range(min(line+1, r-1-line)):
            for j in range(c):
                if(piece[line-k][j] != piece[line+k+1][j]):
                    pos = False
                    break
            
            if(not pos):
                break
        if(pos):
            return line+1
        
    return -1


row_sum = 0
col_sum = 0

for piece in data:
    temp = horizontal_reflection(piece)
    if(temp != -1):
        row_sum += temp
        continue
    temp = vertical_reflection(piece)
    if(temp != -1):
        col_sum += temp

print(100*row_sum+col_sum)


