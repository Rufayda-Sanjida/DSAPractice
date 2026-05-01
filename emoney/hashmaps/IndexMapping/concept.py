

nums = [10, 20, 30, 40, 50]
myMap = {0: 10, 1: 20, 2: 30}

index_map = {}
for i, x in enumerate(myMap):
    print(i, x)
    if x in index_map:
        seenAtDifferentIndex = index_map[x]
    
    index_map[x]