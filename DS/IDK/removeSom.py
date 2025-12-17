nums = [1, 1, 2, 2, 3, 3, 4]

NOTunique = 1

validPointer = 0
searchPointer = 1

while searchPointer < len(nums):
    if nums[validPointer] == nums[searchPointer] and NOTunique < 2:
        NOTunique +=1
        validPointer += 1
    
    if nums[validPointer] != nums[searchPointer]:
        NOTunique = 1
        validPointer += 1 

    if NOTunique > 2:
        NOTunique +=1
    
    if NOTunique > 2 and nums[validPointer] != nums[searchPointer]:
        nums[validPointer] == nums[searchPointer]
        validPointer += 1 

    
    searchPointer += 1