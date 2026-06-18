## 2653. Sliding Subarray Beauty

'''
integerArray = [11, 2, -3, 0, 8]
n = len(integerArray)
subarrays:
[1, 2, 3]
[1]
[1, 2]
[1, 2, 3]
[2]
[2, 3]
[3]

going to be given x = integer

- subarrays must be of size k:


find the beauty of each subarray (thats size k)

beauty: 
the xth smallest number (if x = 2) then the second smallest number 

however many subarrays there are = that many beauty!!

return a list of beauties (all subarrays of length k have beauty)

brute force method:

- get subarray of length k
- calculate the beauty of that subarray 
- append that beauty to a list 
'''


#brute force: 

# nums = [-3,1,2,-3,0,-3]
# k = 2
# p = 1

# beautyList = []

# for x in range(0, len(nums)-k+1):
#     subarray = nums[x: x+k]
#     print()
#     print("before sorting:")
#     print(subarray)


#     print("after sorting: ")
#     # getting the xth smallest

#     #1. sort
#     subarray.sort()
#     print(subarray)

#     # get the pth smallest is 
#     smallestp = subarray[p-1]
#     print("the 2nd smallest is:", subarray[p-1])

#     # if num is greater than 0, beauty is 0 otherwise keep the negative num
#     if smallestp > 0:
#         smallestp = 0
    
#     beautyList.append(smallestp)

# print()
# print(beautyList)



'''
pattern: sliding window
because i need to keep a window of fixed size k
shrink when the window goes above k
add until the window is k 

when window is k then we can find the beauty 

'''

nums = [1,-1,-3,-2,3]
k = 3
x = 2

front = 0
beautyList = []


for finish in range(0, len(nums)):

    # when our window exceeds k: shrink
    while (finish - front + 1) > k:
        front = front + 1

    
    # when our window reaches k:
    if (finish - front + 1) == k:
        # 1. get the xth smallest (or 0)
        subarray = nums[front: finish+1]
        subarray.sort()
        val = subarray[x-1]

        if val > 0:
            val = 0


        # 2. append 
        beautyList.append(val)
    
    
print(beautyList)