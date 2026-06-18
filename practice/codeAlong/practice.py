myArray = [3, 12, 3, 5, 1, 5, -3, 5]
k = 8

myHashmap = {}
count = 0

for x in range(0, len(myArray)):
    value = k - myArray[x]

    if value in myHashmap:
        count = count + myHashmap[value] 
    
    if myArray[x] not in myHashmap:
        myHashmap[myArray[x]] = 1
    else:
        myHashmap[myArray[x]] += 1

print(count)

