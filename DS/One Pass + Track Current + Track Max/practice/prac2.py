#Longest run of same numbers

list1 = [1,1,1,2,2,1] # → 3

maxRun = 1
current = 1

for x in range(1, len(list1)):
    if list1[x-1] == list1[x]:
        current = current + 1
    else:
        current = 1

    if current > maxRun:
        maxRun = current

print(maxRun)
