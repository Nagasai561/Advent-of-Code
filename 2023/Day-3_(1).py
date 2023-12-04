# getting the input from a file
with open("input.txt") as file:
    data = file.read()

# separating lines
data = data.split("\n")


r = len(data)   # number of lines/rows
c = len(data[0])   # number of columns

i = 0   
j = 0
result = 0

while i<r:
    j = 0
    while j<c:
        if(not data[i][j].isdigit()):   # checking if data[i][j] is not a digit
            j += 1                      # if yes, continue
            continue
        symbol_present = False          # boolean flag to mark whether i encountered a symbol around this number
        k = j                           # we will make "k" store the end of current number we are looking at
        while (k < c) and (data[i][k].isdigit()):  # keep increasing "k" till we don't get a digit
            k += 1
        

        if(j > 0):              # if previous columns exist then check for symbols there
            if(data[i][j-1] != '.' and not data[i][j-1].isdigit()):
                symbol_present = True
            if(i > 0 and (data[i-1][j-1] != '.') and not data[i-1][j-1].isdigit()):
                symbol_present = True
            if(i+1 < r and (data[i+1][j-1] != '.')) and not data[i+1][j-1].isdigit():
                symbol_present = True
        
        if(k < c):              # if next column exist then check for symbols there
            if(data[i][k] != '.' and not data[i][k].isdigit()):
                symbol_present = True
            if(i > 0 and (data[i-1][k] != '.') and not data[i-1][k].isdigit()):
                symbol_present = True
            if(i+1 < r and (data[i+1][k] != '.') and not data[i+1][k].isdigit()):
                symbol_present = True

        if(i > 0):              # if previous row exists then check there
            for l in range(j, k):
                if(data[i-1][l] != '.' and not data[i-1][l].isdigit()):
                    symbol_present = True
        
        if(i+1 < r):            # if next row exists then check there
            for l in range(j, k):
                if(data[i+1][l] != '.' and not data[i+1][l].isdigit()):
                    symbol_present = True

        if(symbol_present):     # If I encountered a symbol surrounding this number
            result += int(data[i][j:k])     # Then add the number to the result

        j = k
    i += 1


print(result)   # print the result
            


