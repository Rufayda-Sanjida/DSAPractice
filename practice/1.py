
# integer = both negatives and positives

nums = [25, -1, 0, 45, 7]

target = -7


for x in range(0, len(nums)-1): 
    for j in range(x + 1, len(nums)):
        # if both ranges ending same place then second loop just wont run since x + 1 is range(4, 4)
        # we can make len(nums) -1 to not make it wasteful as we will + 1
        
        #print(nums[x], nums[j])
        product = nums[x] * nums[j]
        if product == target:
            print("indices: " , x, j)

       
## what if i want repeats?? i should get: 1, 4 AND 4, 1

for c in range(0, len(nums)):
    for k in range(0, len(nums)):
        product = nums[x] * nums[j]
        
        if product == target:
            print("indices: " , c, k)






        
'''
return indices of the two numbers such that they add up to target.

- since multiplication is communitive
- we dont necessary need to check two indices twice just once 
- each index paired with every index once 


25 * -1
25 * 0
25 * 45
25 * 7
-1 * 0
-1 * 45
-1 * 7
0 * 45
0 * 7
45 * 7

- nested loop with no repeats!



nums = [1, 2, 3, 4]

print(len(nums)) # 4
print(len(nums)-1) # 3

for x in range(0, len(nums)-1): # 0, 1, 2,  %%%%% when it sees 3 it stops 
    for j in range(x + 1, len(nums)): # range (3, 4) executes 
        print(nums[j])
'''

