array = [1, 2, 3, 4, 5, 6]

count = 0
for x in range(0, len(array)):
    if array[x] % 2 == 0:
        count += 1

print(count)