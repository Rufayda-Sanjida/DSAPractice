#5️ Example 1: LC 674 — Longest Continuous Increasing Subsequence

#Find the length of the longest contiguous increasing subarray

myList = [1, 3, 4, 5, 1, 2, 4, 5, 7]

#hint: longest, biggest, best, continious 


maxNum = 0
current = 1

for x in range(1, len(myList)):

    #is it valid? +1
    if myList[x-1] < myList[x]:
        current = current + 1
    #not valid? restart counter
    else:
        current = 1
    
    #update max
    if maxNum < current:
        maxNum = current

print(maxNum)