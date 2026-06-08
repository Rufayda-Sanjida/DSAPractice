nums = [-4,-1,0,3,10]

front = 0
back = len(nums) - 1

while front < back:
    #whos bigger? 
    frontSquared = nums[front] * nums[front] 
    backSquared = nums[back] * nums[back]
    
    # saveBack = nums[back]
    
    if frontSquared > backSquared:
        nums[back] = frontSquared
        nums[front] = backSquared
    else:
        nums[back] = backSquared
        nums[front] = frontSquared
     
    back = back - 1
    front = front + 1

print(nums)

'''
[-5,-3,-2,-1]

Use Testcase
Output
[1,9,4,25]
Expected
[1,4,9,25]


'''

nums = [-4,-1,0,3,10]


front = 0
back = len(nums) - 1

while front < back:
    #whos bigger? 
    frontSquared = nums[front] * nums[front] 
    backSquared = nums[back] * nums[back]
    
    saveBack = nums[back]
    
    if frontSquared > backSquared:
        nums[back] = frontSquared
        nums[front] = backSquared
    else:
        nums[back] = backSquared
        nums[front] = frontSquared
     
    back = back - 1

print(nums)