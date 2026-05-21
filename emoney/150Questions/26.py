

array = [0,0,1,1,1,2,2,3,3,4]
scannerPointer = 1
holder = 0
k = 1

while scannerPointer < len(array):
    if array[holder] != array[scannerPointer]:
        holder += 1
        array[holder] = array[scannerPointer]
        k += 1
    scannerPointer += 1


print(array[0:k])


def removeDuplicates(nums):
    scannerPointer = 1
    holder = 0

    while scannerPointer < len(nums):
        if nums[holder] != nums[scannerPointer]:
            holder += 1
            nums[holder] = nums[scannerPointer]
        scannerPointer += 1

    return holder + 1



