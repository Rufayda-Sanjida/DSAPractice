#Max value in array

list1 = [1, 91, 4, 5, 1, 6, 7, 2, 1]


largest = list1[0]

for x in range(1, len(list1)):
    if largest < list1[x]:
        largest = list1[x]
    

print(largest)
