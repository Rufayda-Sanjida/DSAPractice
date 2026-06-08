'''
- sorted squares, 

- why is this two pointers?
    - because the largest numbers come from the ends and so we just need to really compare the ends 

'''

numbers = [-12, -4, -1, 0, 3, 10]

#method 1: just sort it by getting the positives of the numbers 

#method 2: two pointers
# front = 0
# end = len(numbers) - 1

# while front != end: 
#     squaredFront = numbers[front] * numbers[front]
#     squaredEnd = numbers[end] * numbers[end]
    
#     if squaredFront > squaredEnd:
#         #Swap
#         holder = numbers[end]
#         numbers[end] = numbers[front]
#         numbers[front] = holder
#     numbers[end] = numbers[end] * numbers[end]
#     end = end - 1

# numbers[front] = numbers[front] * numbers[front]

# print(numbers)


def sortedSquares(nums):
    n = len(nums)
    result = [0] * n  # Prepare an output array

    left = 0
    right = n - 1
    pos = n - 1  # Start filling result from the end

    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left] ** 2
            left += 1
        else:
            result[pos] = nums[right] ** 2
            right -= 1

        pos -= 1

    return result