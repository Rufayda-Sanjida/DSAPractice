
'''

why use? 2 pointers method is for finding unique in sorted list that has duplicates and we use 2 pointers coz its the fastest?
this wont work for finding the duplicates because we do not store them anywhere or else the num[fast-1] part would not work
'''
def removeDuplicates(nums):
    
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

nums = [0, 0, 1, 1, 1, 2, 2, 3, 4, 4]
removeDuplicates(nums)
print(nums)