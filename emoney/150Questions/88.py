
def merge(nums1, m, nums2, n):

    pointer1 = m-1
    pointer2 = n-1
    placeholder = (m + n) - 1

    # i wanna go down the pointers until the list finishes.
    # sometimes one list will finish before the other list so i have to put those remaining numbers in too

    while pointer1 > -1 and pointer2 > -1: #both indices must be 0 and up to continue comparing 
        if nums1[pointer1] > nums2[pointer2]:
            nums1[placeholder] = nums1[pointer1]
            pointer1 -= 1
        else:
            nums1[placeholder] = nums2[pointer2]
            pointer2 -= 1
        
        placeholder -= 1

    # once we finish comparing: clean up if nums1 still has numbers left
    # clean up if nums2 still has numbers left

    while pointer1 > -1:
        nums1[placeholder] = nums1[pointer1]
        pointer1 -= 1
        placeholder -= 1
    
    while pointer2 > -1:
        nums1[placeholder] = nums2[pointer2]
        pointer2 -= 1
        placeholder -= 1

    return nums1


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

print(merge(nums1, m, nums2, n))