#977. Squares of a Sorted Array

'''

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

- sorted = two pointers 
- 10^4 ONE PASS POSSIBLE

'''

nums = [-4,-1,0,3,10]

#nums = [16, 1, 0, 9, 100] 
# Output: [0,1,9,16,100]

front = 0
back = len(nums) - 1

while front < back:
    #whos bigger? 
    frontSquared = nums[front] * nums[front] 
    backSquared = nums[back] * nums[back]
    
    saveBack = nums[back]
    
    if frontSquared > backSquared:
        nums[back] = frontSquared
        nums[front] = saveBack
    else:
        nums[back] = backSquared
    
    back = back - 1

print(nums)
