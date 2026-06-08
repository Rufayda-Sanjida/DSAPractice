#ONLY for sorted list!
#is it worth doing binary search when you're given an unsorted list?
# if its only 1 search, its not worth sorting it just do linear search!
# repeated searches = binary search!


# def binarysort(array, target):
#     middle = len(array) // 2
#     if array[middle]== target:
#         return(f'Found the target at index {middle}')
#     else:
#         if array[middle] > target:
#             binarysort(array[0:middle], target)
#         else:
#             binarysort(array[middle:], target)

# print(binarysort([1, 2, 3, 4], 1))

def binarysearch(nums, target):
    left = 0 # first index
    right = len(nums)-1    #last index             

    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target: #search right half
            left = mid + 1
        else:
            right = mid - 1 # search left half
    return -1

print(binarysearch([1, 2, 3, 4, 5, 6, 7], 6))



def binarysearch(nums, target):
    
    left = 0
    right = len(nums)-1
    
    while left <= right:
        middle = (left + right) // 2
        
        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1