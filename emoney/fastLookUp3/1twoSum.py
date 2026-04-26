# Return indices of two numbers that add up to target.
# hashmap fast loop up concept coz im thinking of pairs in an unsorted array

# Input: 
nums = [2,7,11,15]
target = 9

# Output: [0,1]

def twoSum(nums, target):
    seen = {}

    for x in range(0, len(nums)):
        total = target - nums[x] 
        
        if total in seen:
            return(x, seen[total])
        else:
            seen[nums[x], x]

