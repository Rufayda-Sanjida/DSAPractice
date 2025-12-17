#1. Find the Maximum Sum of Any Window of Size K

# nums = [1,2,3,4,5]
# k = 3

# largest = 0
# front = 0
# sum = 0
# largestList = []

# for x in range(0, len(nums)):
#     #sum gets updated every 3 and the front is subtracted!
#     largestList.append(nums[x])
#     sum = sum + nums[x]

#     if x - front >= k:
#         sum = sum - nums[front]
#         largestList.pop(0)
#         front = front + 1

#     if largest < sum:
#         largest  = sum 

# print(largest) 
# print(largestList)



nums = [1,2,3,4,5]
k = 3
sum = 0
largest = 0
front = 0
for back in range(0, len(nums)):
    
    windowSize = (back - front) + 1

    if windowSize <= 3:
        sum = sum + nums[back]
    if windowSize == 3:
        if largest < sum:
            largest = sum 
    else:
        sum = sum - nums[front]
        front = front + 1