
with open("input.txt", 'r') as file:
    data =  file.read()

data = data.split("\n")


result = 0
r = len(data)   # number of rows
c = len(data[0])    # number of columns

for i in range(r):
    for j in range(c):
        if(data[i][j] != '*'):
            continue

        num_list = []   # we will check if there is any adjacent number to the "*", if there is we will append it to this list

        # checking for number that is at right side of "*"
        if((j+1 < c) and (data[i][j+1].isdigit())):
            right = j+1
            while((right < c) and (data[i][right].isdigit())):
                right += 1
            num_list.append(data[i][j+1:right])
        
        # checking for number that is at left side of "*"
        if((j > 0) and (data[i][j-1].isdigit())):
            left = j-1
            while((left >= 0) and (data[i][left].isdigit())):
                left -= 1
            num_list.append(data[i][left+1: j])

        # checking for numbers that occupy top left sqaure
        if((i > 0) and (j > 0) and (data[i-1][j-1].isdigit())):
            left = j-1
            right = j-1
            while((left >= 0) and (data[i-1][left].isdigit())):
                left -= 1
            while((right < c) and (data[i-1][right].isdigit())):
                right += 1
            num_list.append(data[i-1][left+1:right])
        
        # checking for numbers that start at just top square and doesn't occupy top left square
        if((i > 0) and data[i-1][j].isdigit()): 
            if((j > 0) and data[i-1][j-1].isdigit()):
                pass
            else:
                right = j
                while((right < c) and data[i-1][right].isdigit()):
                    right += 1

                num_list.append(data[i-1][j:right])
    
        # checking for numbers that start at top right square
        if((i > 0) and (j+1 < c) and (data[i-1][j+1].isdigit())):
            if(data[i-1][j].isdigit()):
                pass
            else:
                right = j+1
                while((right < c) and data[i-1][right].isdigit()):
                    right += 1
                num_list.append(data[i-1][j+1:right])

        # checking for numbers that caontain bottom left square
        if((i+1 < r) and (j > 0) and (data[i+1][j-1].isdigit())):
            left = j-1
            right = j-1
            while((left >= 0) and (data[i+1][left].isdigit())):
                left -= 1
            while((right < c) and data[i+1][right].isdigit()):
                right += 1
            num_list.append(data[i+1][left+1: right])   

        # checking for numbers that contain bottom square without bottom left square
        if((i+1<r) and data[i+1][j].isdigit()):
            if((j > 0) and data[i+1][j-1].isdigit()):
                pass
            else:
                right = j
                while((right < c) and data[i+1][right].isdigit()):
                    right += 1
                num_list.append(data[i+1][j:right])

        # checking for numbers that start from bottom right square
        if((i+1 < r) and (j+1 < c) and data[i+1][j+1].isdigit()):
            if(data[i+1][j].isdigit()):
                pass
            else:
                right = j+1
                while((right < c) and data[i+1][right].isdigit()):
                    right += 1
                num_list.append(data[i+1][j+1: right])


        # checking is done
        if(len(num_list) == 2):
            result += float(num_list[0])*float(num_list[1])

print(result)
            