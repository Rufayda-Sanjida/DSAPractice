#NO DUPLICATES + MUTABLE 
# No index system 

s = {1, 2, 3}
makingSet = set()

# 1. Add element
s.add(3)

# 2. transform list with duplicates into set to remove duplicates
nums = [1,1,2,3]
unique = set(nums) # unique = {1,2,3}

def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True
        
        seen.add(num)

    return False

print(containsDuplicate([1, 2, 3, 4]))