nums = [1,3,5,4,7]

largest = 1
current = 1

for x in range(0, len(nums)-1):

    if nums[x] < nums[x + 1]:
        current = current + 1
    else:
        current = 1
    
    if largest < current:
        largest = current

print(largest)
