with open("input.txt", 'r') as file:
    data = file.read()

data = data.split(",")  # separate the string wrt ','

result = 0  # variable to store result

for word in data:   # for each word
    temp_result = 0 # temp result
    for char in word:   # find the hash number for this word and add it to result
        temp_result += ord(char)
        temp_result *= 17
        temp_result %= 256
    result += temp_result

print(result)
    