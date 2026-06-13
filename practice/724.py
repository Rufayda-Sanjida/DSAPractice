# 724. Find Pivot Index 

'''
given = nums = [-2, 4, 0, 23, -35] integers

return pivot index:

- the subarray to the left of pivot index equals the subarray to the right of pivot index

- for each index: 
    1. find the subarray to the right 
    2. find the subarray to the left
    3. find the sum of both subarrays
    4. compare them!

- if x == 0 then the subarray to the left == 0
- if x == len(nums)-1 then the subarray to the right == 0

'''

nums = [2,1,-1]

for x in range(0, len(nums)):
    


    rightSubarraySum = 0
    leftSubarraySum = 0
    
    if x == 0:
        leftSubarraySum = 0
        
        for j in range(x + 1, len(nums)):
            rightSubarraySum = rightSubarraySum + nums[j]

    elif x == len(nums) - 1:
        rightSubarraySum = 0
        
        for p in range(0, x):
            leftSubarraySum  = leftSubarraySum + nums[p]

    else:
        # get leftSubarray sum 
        for i in range(0, x):
            leftSubarraySum = leftSubarraySum + nums[i]
        
        # get rightSubarray sum 
        for e in range(x + 1, len(nums)):
            rightSubarraySum = rightSubarraySum + nums[e]
    
    if leftSubarraySum == rightSubarraySum:
        print(x)

       

        
       
