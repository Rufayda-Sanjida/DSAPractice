'''
Q: “Does any element appear more than 3 times?”
this pattern is frequncy map coz we are looking at how many of each element are


If I only care about existence, not counts, do I still use a map?
yes but i exit once i get my value
'''


array = [1, 2, 4, 4, 3, 1, 4, 4, 5, 6, 6, 7, 8]
hashmap1 = {}

#first store and as you go on see if there is already 3 or more in them

for x in range(len(array)):
    if array[x] not in hashmap1:
        hashmap1[array[x]] = 1
    else:
        hashmap1[array[x]] += 1
        if hashmap1[array[x]] > 3:
            print(f"this element has appeared more than 3 times first and that element is {array[x]}")
            break

