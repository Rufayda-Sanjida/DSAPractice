#Example 2: LC 121 — Best Time to Buy and Sell Stock


#hint: best value over a contiguous range (range smallest and biggest profit after)
'''
You don't need to remember everything

Only what's happening now and what was best before

O(n) is optimal and expected
'''

nums = [7,6,4,3,1]
min = 0
maxProfit =  0

for x in range(1, len(nums)):
    
    if nums[min] > nums[x]:
        min = x
    
    #is this the best day to sell stock?
    if maxProfit < nums[x] - nums[min]:
        maxProfit = nums[x] - nums[min]
    

print(maxProfit)