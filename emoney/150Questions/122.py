## 122. Best Time to Buy and Sell Stock II

## second attempt:

'''
I can buy and sell multiple times a day. I need the maximum amount of profit. Everytime there is profit i am just gonna add it to my profit
'''

nums = [1,2,3,4,5]

profit = 0

for x in range(1, len(nums)):

    if nums[x-1] < nums[x]:
        profit = profit + (nums[x] - nums[x-1])





'''

this is very convulted and looks like sell stock I:
core difference: stock I is for minimum seen so far while stock II is local minimum
- everyday i just wanna sell if its lower than before!!! super greedy

- trigger for stock II:
    - multiple transactions

profit = 0

smallestSeenIndex = 0

nums = [7,6,8,3,1]

for x in range(0, len(nums)):

    if nums[x] < nums[smallestSeenIndex]:
        smallestSeenIndex = x
    
    if nums[x] > nums[smallestSeenIndex]: #replace with else
        profit = profit + (nums[x] - nums[smallestSeenIndex])
        smallestSeenIndex = x 


print(profit)


This is simplified to show we really do not need to keep track of smallest so rigoursly
since looking at the previous day works perfectly since
since we 
    1. can take every small gain 
    2. each smaller can be today so previous small can be discarded

profit = 0

smallestSeenIndex = 0

nums = [7,6,8,3,1]

for x in range(0, len(nums)):
    
    if nums[x] > nums[smallestSeenIndex]: #replace with else
        profit = profit + (nums[x] - nums[smallestSeenIndex])
    
    smallestSeenIndex = x 


print(profit)

'''


nums = [1, 3, 5, 2, 9]
profit = 0

for x in range(1, len(nums)):

    if nums[x] > nums[x-1]:
        profit = profit + (nums[x] -  nums[x-1])
    