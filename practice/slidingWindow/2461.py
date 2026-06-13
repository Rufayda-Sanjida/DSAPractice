# 2461. Maximum Sum of Distinct Subarrays With Length K

'''

integerArray = [1, 2, 3, 4]
integerK = k (length of subarray)

- find all length 3 subarrays from array
- ask if those elements in the subarray are distinct??
    - if distinct ? find sum
        - if sum greater than largestSum seen so far -> replace sum
    - if not distinct -> next subarray

'''

nums = [1,5,4,2,9,9,9]
k = 3

largestSum = 0

for x in range(0, len(nums)):
    for j in range(x + 1, len(nums)+1):
        if len(nums[x:j]) == k:
            print(nums[x:j])
        
        # are those elements in nums[x:j] distinct????
        
        #hashmap of what ive seen before -> if ive seen it? exit loop
        seenBefore = False
        hashmap = {}
        for i in nums[x:j]:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                seenBefore = True
                break
        
        #if distinct -> get the sum
        mySum = 0
        if seenBefore == False:
            for p in nums[x:j]:
                mySum = mySum + nums[p]
        
        if mySum > largestSum:
            largestSum = mySum

        


# or 
'''

nums = [1,5,4,2,9,9,9]
k = 3
for x in range(0, len(nums)):
    for j in range(x, len(nums)):
         print(nums[x:j+1])

'''
