'''

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
'''

oneCounter = 0
maxOneCounter = 0
listNum = [1,0,1,1,0,1]
for x in range(0, len(listNum)):
    if listNum[x] == 1:
        oneCounter += 1
    
    if listNum[x] == 0 or x == len(list)-1 : #last digit
        if maxOneCounter < oneCounter:
            maxOneCounter = oneCounter
            oneCounter = 0









nums = [1,1,0,1,1,1]
counter = 0
max1 = 0

for x in range(0, len(nums)):
    if nums[x] == 1:
        counter = counter + 1
    
    if nums[x] == 0:
        if max1 < counter:
            max1 == counter
        counter = 0

    if x == len(nums)-1:
        if max1 < counter:
            max1 == counter

#we can combine the last 2: last attempt^

# nums = []
# counter = 0
# maxCounter = 0

# for x in range(0, len(nums)):
#     if nums[x] == 1:
#         counter+=1 
#     if nums[x] == 0 or x == len(nums)-1: #if we are at the end of the list 
#         if counter > maxCounter:
#             maxCounter = counter
#         counter = 0
        
# print(maxCounter)