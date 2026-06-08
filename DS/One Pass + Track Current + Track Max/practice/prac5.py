#Largest Sum of Contiguous Positive Numbers
#hint = largest + contigious

num = [1,2,-3,4,5, 2] #→ 9

#when you see - then you reset the counter to 0
# only care about what you have seen so far and the best and compare update no worry about the future

currentSum = 0
largestSum = 0

for x in range(0, len(num)): 
    if num[x] > 0:
        currentSum = currentSum + num[x]
    else:
        currentSum = 0
    
    if largestSum < currentSum:
        largestSum = currentSum 

print(largestSum)