# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

nums = [0,1,0,3,12]

for x in range(0, len(nums)):
   if nums[x] == 0:
       nums.append(0)
       nums.pop() 