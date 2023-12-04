# I have saved the input in a file called "input.txt"
# Loading the file into python
with open("input.txt", 'r') as file:
    text = file.read()


result = 0      # to store the answer

for line in text.split("\n"):   #each line in the string "text" is separated by a newline, so we will split on it
    digits_seen = []            #storing all the digits seen in a list
    for char in line:
        if(char.isdigit()):
            digits_seen.append(int(char))

    result += digits_seen[0]*10 + digits_seen[-1]     #getting the first and last digit seen and making it into two digit number

print(result)
    