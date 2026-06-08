## 53. Maximum Subarray

# Given an integer array nums, find the subarray with the largest sum, and return its sum.

nums = [-2,1,-3,4,-1,2,1,-5,4]

currenSum = nums[0]
bestSeenSoFar = currenSum

for x in range(1, len(nums)):
    # should i scrap what i used to have and start fresh? current INDEX > sum + current index
    total = currenSum + nums[x]

    if nums[x] > total:
        currenSum = nums[x]
    else:
        currenSum = total

    if currenSum > bestSeenSoFar:
        bestSeenSoFar = currenSum

    # should i continue with what i have? = sum + current index > current index alone

print(bestSeenSoFar)