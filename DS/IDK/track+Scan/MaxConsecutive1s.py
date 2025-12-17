nums = [1,1,0,1,1,1]

largest = 0
count = 0

for x in range(0, len(nums)):

    if nums[x] == 1:
        count = count + 1
    else:
        count = 0
    
    if largest < count:
        largest = count
