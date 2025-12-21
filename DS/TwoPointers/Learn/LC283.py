#LC 283 — Move Zeroes (Same Direction)

'''
Goal:

Move all 0s to end

Keep order of non-zero
'''


nums = [1, 0, 2, 0, 3, 0, 4, 5]


pointer1 = 0

for x in range(0, len(nums)):
    if nums[x] != 0:
        holder = nums[pointer1]
        nums[pointer1] = nums[x]
        nums[x] = holder
        pointer1 += 1

print(nums)



# nums = [1, 0, 2, 0, 3, 0, 4, 5]


# pointer1 = 0

# for x in range(0, len(nums)):
#     if nums[x] != 0:
#         nums[pointer1] = nums[x]
#         nums[x] == 0
#         pointer1 += 1

# print(nums)


