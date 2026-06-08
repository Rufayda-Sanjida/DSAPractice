# 713. Subarray Product Less Than K


'''
Given an array of integers nums and an integer k, 
return the number of contiguous subarrays where the product 
of all the elements in the subarray is strictly less than k.

given: 
integer nums = [-2, 45, 0, 1, -33] 
integer k = 4 

solution:
- find all the contiguous subarrays
- find the product of all the elements in the contigious subarrays
- find out if the product is less than k 

'''


nums = [1,2,3]
k = 0

count = 0
for x in range(0, len(nums)):
    for j in range(x + 1, len(nums) + 1):
        #print(nums[x: j])

        product = 1
        for p in range(x, j):
            product = product * nums[p]
        
        #print("product ", product)

        if product < k:
            count = count + 1

print(count)
