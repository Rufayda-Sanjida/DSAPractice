nums = [1, 2, 3, 1]
k = 3

indexDict = {}

for x in range(0, len(nums)):

    if nums[x] in indexDict:
        #stores the index where I saw it
        if x - indexDict[nums[x]] <= 3:
            print("We found it!")
    
    indexDict[nums[x]] = x #store last seen
        

