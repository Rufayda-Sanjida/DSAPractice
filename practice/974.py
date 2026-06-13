'''


'''

nums = [5]
k = 9

count = 0
for x in range(0, len(nums)):
    for j in range(x + 1, len(nums)+1):

        sum = 0
        for p in range(x, j):
            sum = sum + nums[p]
        
        # sum divisible by k 
        if sum % k == 0:
            count = count + 1
            
print(count)