# Goal: Return True if duplicate values are at most k distance apart.

input = [1, 2, 3, 4]
k = 3
mySet = set()

def function(input, k):
    
    for x in range(0, len(input)):
        if input[x] in mySet:
            return True

        mySet.add(input[x])

        if len(mySet) > k:
            #mySet.remove(0) theres no such thing as positions in sets 
            mySet.remove(input[x-k])

    return False
