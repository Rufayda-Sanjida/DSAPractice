
def removeElement(nums, val):
    holder = 0 #stationed where the numbers we want aka unique
    scanningPointer = 0
    k = 0

    while scanningPointer < len(nums):
        if nums[scanningPointer] != val:
            nums[holder] = nums[scanningPointer]
            holder += 1
            k += 1
        scanningPointer += 1

    # print(nums[0:k])
    # print(k)
    return k


nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))

'''
run time = 0(n)
n being the number of elements -> scanner pointer scans the whole list once!

space time complexity = 0(1) no extra space
'''