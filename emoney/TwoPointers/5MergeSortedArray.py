'''
two sorted integer arrays nums1 and nums2, with nums1 having enough trailing 
space to hold elements from both arrays, the task is to merge nums2 into nums1 
so that the resulting array remains sorted.

the arrays are given with their valid lengths m and n, and the final sorted output 
must be stored directly in nums1.


'''

nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]

m = 3
n = len(nums2)

# we start at the end 
handler = len(nums1) - 1
pointer1 = m - 1
pointer2 = n - 1 

while pointer1 >= 0 and pointer2 >= 0:
    #comparision
    first = nums1[pointer1]
    second = nums2[pointer2]
    if nums1[pointer1] > nums2[pointer2]:
        nums1[handler] = nums1[pointer1]
        pointer1 = pointer1 - 1
    else: #pointer1[m] < pointer2[n]
        nums1[handler] = nums2[pointer2]
        pointer2 = pointer2 - 1
    
    handler = handler - 1

print(nums1)