#C2. Longest Subarray With Positive Product

'''
longest + subarray = one pass find current and compare to max 
no care about future only about what has happened so far at that index  
'''

nums = [-1,2]

maxPosProductLength = 0
posLength = 0
negLength = 0
negProduct = 1

for x in nums:
    
    if x == 0:
        posLength = 0
        negLength = 0
        negProduct = 1
        continue
    
    negProduct = negProduct * x
    
    if x > 0:
        posLength = posLength + 1
    else:
        posLength = 0
    
    negLength = negLength + 1

    if negProduct > 0:
        if maxPosProductLength < negLength:
            maxPosProductLength = negLength
    
        if maxPosProductLength < posLength:
            maxPosProductLength = posLength


print(maxPosProductLength)