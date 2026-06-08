'''
Goal: Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
hints: -s orted, 

numsSquared = [4, 1, 0, 3, 10]
numsSquared = [0, 1, 3, 4, 10]
numsSquared = [0, 1, 9, 16, 100]
'''


'''
Input: nums = [-4,-1,0,3,10] -> [16, 1, 0, 9, 100]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100]
'''

nums = [-4,-1,0,3,10]
print(nums)

print(abs(nums[0]))
front = 0
back = len(nums)-1

print(f"front {front}")
print(f"back {back}")

while front < back:
    if abs(nums[back]) < abs(nums[front]):
        # print("Condition met")
        # print(f"front {abs(nums[back])}")
        # print(f"back {abs(nums[front])}")
        #swap
        temp = abs(nums[front])
        nums[front] = abs(nums[back])
        nums[back] = temp * temp
    back = back - 1

nums[1] = nums[1] * nums[1]
print(nums)