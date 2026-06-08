'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums. Return k.

Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
'''


# output: [1, 3, 4, 5, _, _] ; 4 ; 4 elements are not equal to val
# hint: use slow fast method 2 pointers

#concept slow fast method:
#slow holds spot at 1 and fast starts at 1 and goes on until it finds something before it that doesn't match up and thats when you replace the slow AND slow increment by 1
nums = [1, 2, 2, 3, 4, 2, 5, 2, 6]
print(nums)
val = 3
slow = -1

for fast in range(0, len(nums)): #len(nums) is not included so it gets all the elements
    if nums[fast] != val:
        slow = slow + 1
        nums[slow] = nums[fast]

print(nums[0:slow+1]) #it leaves the duplicates tho!!!!