'''
Goal: find the number of unique elements in a sorted list that contains duplicates (so the duplicates are right next to each other)
logic: We loop through with one pointer finding the first occurence of each number (aka unique value) and once we find it, we make it equal to the pointer slow is standing and increment. Slow will be keeping track of the unique elements only moving forward whenever its replaced.
why use? 
- sorted array
- 2 pointers where 1 moves fast (finding unique values) and the other moves slow (keeps track of new orgaanized list) this only works because we are NOT swapping but simply replacing the value of slow and the fast[n-1] is the same and can be accurately compared. 
'''
def removeDuplicates(nums):
    
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

nums = [1, 2, 2, 2, 3, 4, 4]
removeDuplicates(nums)
print(nums)