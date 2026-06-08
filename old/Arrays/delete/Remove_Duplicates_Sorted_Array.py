'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

'''


nums = [1,1,2]
count = 1


i = 1
while i < len(nums): 
    if nums[i] == "_":
        break
    elif nums[i] == nums[i-1]:
        nums.pop(i)
        nums.append("_")
    else:
        count = count + 1
        i += 1
  
print(nums) 
print(count)     
#when you append to list while looping, must break
#when you wanna skip some steps = while loop
    
    
#last attempted:

# for x in range(1, len(nums)):
#     if nums[x] == nums[x-1]:
#         nums.pop(x)
#         nums.append("_")
#     else:
#         count = count + 1
     
# # sometimes i dont want it to loop coz i sometimes do not want to increment every time; sometimes i dont want to increment especially when i delete an element 
# # deleting element; i probably shouldnt use a for loop; while loop; i can control when i increment   
# print(nums)
# print(count)