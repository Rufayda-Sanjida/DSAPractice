# 523. Continuous Subarray Sum

'''
- we are given:
integer array = nums = [-1, 4, 0, -30, 19]
integer k = 4

- we are looking for a good subarray (just one)
- whats a subarray??
[1, 2, 3]

[1]
[1, 2]
[1, 2, 3]
[2]
[2, 3]
[3]

- do i know how to find all the subarrays of an array? GENERATE ALL SUBARRAYS
- IS IT POSSIBLE TO GENERATE SUBARRAYS 
- get only subarrays that are lenghth 2 and higher
- can you sum them?
- is the sum a multiple of k??
print(9 % 3 == 0) BIG NUMBER % Number == 0 -> multiple : big number is a multiple of number
ex. 21 is a multiple of 3 because 21 % 3 == 0 ; 3 cleanly fits in 21 7 times

'''

nums = [1, 2, 3]
k = 3
for x in range(0, len(nums)):
    for j in range(x + 2, len(nums)+1):
        sum = 0
        for z in range(x, j): # this works coz j is not includedddddd exclusive!!!
            sum = sum + nums[z]
        
        if (sum % k == 0):
            print(sum)
            print(nums[x: j])

        #print(nums[x: j]) 
        #print(sum)





'''
what does it mean to be a multiple of a number?
multiple of a number means that that number can get inside that number 1 or multiple times evenly divide!!
2 * 3 is just 2 + 2 + 2
3 * 3 = 3 + 3 + 3

evenly get in!!!

'''



'''

nums = [1, 2, 3]

for x in range(0, len(nums)):
    for j in range(x + 1, len(nums)+1):
        print(nums[x], nums[j]) 

        #### this fails because nums[j] len(nums)+1 IS GETTING TO INVALID TERRIROTUR 

'''




