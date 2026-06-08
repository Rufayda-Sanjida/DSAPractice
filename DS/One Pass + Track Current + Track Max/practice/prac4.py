#Max Difference (Later − Earlier)

'''
max difference: 
hint: something max
only worry about what we have seen and compare it to present! no worry about the future
'''

maxDifference = 0
smallest = 0
nums = [9, 8, 7, 6]


for x in range(1, len(nums)):
    
    if nums[x] < nums[smallest]:
        nums[smallest] = nums[x]
    
    if nums[x] - nums[smallest] > maxDifference:
        maxDifference = nums[x] - nums[smallest]

print(maxDifference)

