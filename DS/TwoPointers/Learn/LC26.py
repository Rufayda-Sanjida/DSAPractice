#LC26. Remove Duplicates from Sorted Array

'''
- Hints: "sorted", "remove", we are in place modication 
- in place since 10^4 is limit of inputs
'''

nums = [0,0,1,1,1,2,2,3,3,4]
pointer1 = 0

for x in range(1, len(nums)):
    
    if nums[x-1] != nums[x]:
        pointer1 = pointer1 + 1
        nums[pointer1] = nums[x]


print(nums)
print(pointer1+1)


