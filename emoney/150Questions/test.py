arr = [7, 1, 5, 3, 6, 4]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        print(f"i={i}, j={j}, arr[i]={arr[i]}, arr[j]={arr[j]}")