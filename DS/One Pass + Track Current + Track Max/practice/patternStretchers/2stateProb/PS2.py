#C2. Longest Subarray With Positive Product

'''
longest + subarray = one pass find current and compare to max 
no care about future only about what has happened so far at that index  
'''

# nums = [-1,2]

# maxPosProductLength = 0
# posLength = 0
# negLength = 0
# negProduct = 1

# for x in nums:
    
#     if x == 0:
#         posLength = 0
#         negLength = 0
#         negProduct = 1
#         continue
    
#     negProduct = negProduct * x
    
#     if x > 0:
#         posLength = posLength + 1
#     else:
#         posLength = 0
    
#     negLength = negLength + 1

#     if negProduct > 0:
#         if maxPosProductLength < negLength:
#             maxPosProductLength = negLength
    
#         if maxPosProductLength < posLength:
#             maxPosProductLength = posLength


# print(maxPosProductLength)


nums = [0, 1, -2, -3, -4]

posLen = 0
negLen = 0
best = 0

for x in nums:
    if x == 0:
        posLen = 0
        negLen = 0
    
    elif x > 0:
        posLen += 1
        
        if negLen > 0:
            negLen = negLen + 1
        else: 
            negLen = 0
    
    else:  # x < 0
        if negLen > 0:   
            newPos = negLen + 1 
        else:
            newPos = 0
        newNeg = posLen + 1
        posLen = newPos
        negLen = newNeg

    best = max(best, posLen)

print(best)
