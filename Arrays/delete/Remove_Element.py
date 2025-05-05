'''
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return 
the number of elements in nums which are not equal to val.
'''

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

nums = [0,1,2,2,3,0,4,2]
val = 2

i = 0
count = 0

while i < len(nums):
    if nums[i] == "_":
        break
    elif nums[i] == val:
        nums.pop(i)
        nums.append("_")
    else:
        i = i + 1
        count = count + 1
        
        
print(nums)
print(count)

# #example of nested loops:
# num = [1, 2, 3, 4, 5]
# for x in range(0, len(num)):
#     for i in range(x + 1, len(num)):
#         print(num[x], num[i])
        
# nested loop example: each element gets to be side by side of themselves and each teammember
# and there are repeats too! '

