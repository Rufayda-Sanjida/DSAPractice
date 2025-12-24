#977. Squares of a Sorted Array

'''

Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

- sorted = two pointers 
- 10^4 ONE PASS POSSIBLE

'''

nums = [-5,-3,-2,-1]


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

nums[front] =  nums[front] * nums[front]
print(nums)
l;fsdjglkdfjglkdfjgfd