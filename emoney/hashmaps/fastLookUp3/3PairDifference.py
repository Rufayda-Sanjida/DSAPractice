
#find Pair With Given Difference


def difference(nums, target):

    seen = {}

    for x in range(0, len(nums)):
        numberAdded = nums[x] + target
        numberSubed = nums[x] - target
        
        if numberAdded in seen or numberSubed in seen:
            return True
        else:
            seen[x] = x

    return False

print(difference([1,5,3,4,2], 200))