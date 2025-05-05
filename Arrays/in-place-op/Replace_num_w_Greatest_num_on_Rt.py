arr = [17,18,5,4,6,1]

for x in range(0, len(arr)):
    if x == len(arr)-1:
        arr[x] = -1
        break
    largest = arr[x+1]
    for j in range(x+2, len(arr)):
        if largest < arr[j]:
            largest = arr[j]
    arr[x] = largest

print(arr)