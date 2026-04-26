'''
same two sum problem: array is SORTED
Input: [2,7,11,15], target = 9
Output: [1,2]  # 1-based indexing
'''

# sorted array + pair => Two pointers 


# output : [1,2] 

def twoSum2(inputList, target):

    left = 0
    right = len(inputList)-1

    while left < right:
        result = inputList[left] + inputList[right]
        
        if result == target:
            return (left + 1), (right + 1)
        
        if result < target:
            left = left + 1
        else:
            right = right - 1

    return (-1, -1)

print(twoSum2([2,7,11,15], 9))