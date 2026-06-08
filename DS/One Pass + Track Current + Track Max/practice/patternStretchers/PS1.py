#C1. (LC 485) Maximum Consecutive Ones

nums = [1,1,0,1,1,1] # → 3


largestRepeatingOnes = 0
currentCount = 0

for x in range(0, len(nums)):
    if nums[x] == 1:
        currentCount = currentCount + 1
    else:
        currentCount = 0
    
    if largestRepeatingOnes < currentCount:
        largestRepeatingOnes = currentCount

print(largestRepeatingOnes)
