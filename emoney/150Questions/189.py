# 189. Rotate Array


# find index for all the new numbers depending on k!

# rotatedNums = []
# for x in nums:
#     rotatedNums.append(x)

# for x in range(0, len(nums)):
#     newIndex = (x + k) % len(nums)
#     rotatedNums[newIndex] = nums[x]

# print(nums)
# print(rotatedNums)
'''

leftOver = len(nums) - x
modThis = k-leftOver
betterIndex = modThis % len(nums)

subtraction works! but so does just adding to k aka how much extra we gotta move since our starting index is not 0

thats why we can just do:

x + k -> we can always pretend to start in the beginning and adding x is like adding where the 
current index is coz we are simply trying to wrap the index around to see where it would fall

'''


nums = [1,2,3,4,5,6,7]
k = 3


def rotate(nums, k):
    rotatedNums = []
    for x in nums:
        rotatedNums.append(x)

    for x in range(0, len(nums)):
        newIndex = (x + k) % len(nums)
        rotatedNums[newIndex] = nums[x]
    
    nums[:] = rotatedNums

    return nums


print(rotate(nums, k))