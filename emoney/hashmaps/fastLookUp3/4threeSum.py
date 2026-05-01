# Find all triplets that sum to 0.

# hashmaps get crazy 
# even tho its not sorted -> it can become a two pointer problem after its sorted
# AND first index is the number 


target = 0

def threeSum(nums, target):

    for x in range(0, len(nums)):

        stableNum = nums[x]

        
