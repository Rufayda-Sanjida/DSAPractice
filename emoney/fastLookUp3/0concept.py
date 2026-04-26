# Sub-Pattern C — Fast Lookup (Pair Problems)

"""
While iterating, you store values you've seen so you can instantly check: 
👉 “Does the number I need already exist?”

compute the complement
check it in a hashmap → O(1)
"""

# find two numbers that meet a condition
def twoSum(nums, target):
    seen = {} 

    for i in range(len(nums)):
        complement = target - nums[i] 

        if complement in seen:
            return [seen[complement], i] 
        
        seen[nums[i]] = i
    

