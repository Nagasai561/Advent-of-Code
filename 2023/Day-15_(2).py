def hashmap(s):     # given a label, this function computes the number of box it represents
    ans = 0
    for char in s:
        ans += ord(char)
        ans *= 17
        ans %= 256
    return ans

    
with open("input.txt", 'r') as file:
    data = file.read()

data = data.split(",")

boxes = [[] for i in range(256)]    # we are creating a list whose entries represent each box

for word in data:   # for each word in the input
    if('=' in word):    # if the word contains '='
        label, focal_length = word.split("=")   # split the word at the point of occurence of '='
        number_of_box = hashmap(label)          # and retrieve the focal length and label of the lens
        
        found = False
        for i in range(len(boxes[number_of_box])):  # checking if a lens with same label exists in that box
            if(boxes[number_of_box][i][0] == label):
                boxes[number_of_box][i][1] = focal_length   # if yes, then replace it
                found = True
                break
        
        if(not found):      # if no, then just append it to the end
            boxes[number_of_box].append([label, focal_length])

    else:               # if the word contains '-'
        label = word[:-1]   # retreive the label
        number_of_box = hashmap(label)  # get the number of box, the label represents

        for i in range(len(boxes[number_of_box])):
            if(boxes[number_of_box][i][0] == label):    # if a find a label matching in the box, then remove it
                boxes[number_of_box].remove(boxes[number_of_box][i])
                break

total_power = 0     # storing the final result
for box in range(256):
    for i, lens in enumerate(boxes[box]):   # for each lens, we are adding up it's power to total power 
        power_lens = 0
        power_lens = box+1
        power_lens *= i+1
        power_lens *= int(lens[1])
        total_power += power_lens
    
print(total_power)





