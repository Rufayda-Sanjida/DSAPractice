#Count Characters in a String

input =  "banana"
#output = dictionary with character counts

dictionary = {}

for x in input:
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] += 1