nums = [1, 2, 3, 4, 2, 10, 2, 5, 2, 9]
val = 2


sortedPointer1 = 0
pointer2 = 0

while pointer2 < len(nums):
    if nums[pointer2] != val:
        nums[sortedPointer1] = nums[pointer2]
        sortedPointer1 += 1
    
    pointer2 += 1

print(nums[0:sortedPointer1])
print(sortedPointer1)
