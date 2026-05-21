# Remove Duplicates from Sorted Array II
nums = [0,0,1,1,1,1,2,3,3]

holder = 0
scanner = 1
validDuplicate = True

while scanner < len(nums):
    # IF scanner picks up new: add to holder + validDuplicate = True
    # If scanner picks up old BUT validDuplicate == True : add to holder + validDuplicate = False

    if nums[holder] == nums[scanner] and validDuplicate == True:
        holder += 1
        nums[holder] = nums[scanner] 
        validDuplicate = False

    elif nums[holder] != nums[scanner]:
        holder += 1
        nums[holder] = nums[scanner] 
        validDuplicate = True
    
    scanner += 1


print(nums[0:holder+1])


def removeDuplicates(nums):
    holder = 0
    scanner = 1
    validDuplicate = True

    while scanner < len(nums):
        # IF scanner picks up new: add to holder + validDuplicate = True
        # If scanner picks up old BUT validDuplicate == True : add to holder + validDuplicate = False

        if nums[holder] == nums[scanner] and validDuplicate == True:
            holder += 1
            nums[holder] = nums[scanner] 
            validDuplicate = False

        elif nums[holder] != nums[scanner]:
            holder += 1
            nums[holder] = nums[scanner] 
            validDuplicate = True
        
        scanner += 1
    
    return (holder+1)


print(removeDuplicates([0,0,1,1,1,1,2,3,3]))