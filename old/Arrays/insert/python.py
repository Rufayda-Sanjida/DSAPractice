# # nums = [1,1, 0,1,1,1]

# # maxCounter = 0
# # counter = 0

# # for x in range(0, len(nums)): #this is good coz the len will give OUTSIDE the list for indexing since we start at 0 and range is non inclusive for second number
# #     if nums[x] == 1:
# #         counter+= 1
# #     if nums[x] == 0 or x == len(nums)-1: #if we are at the last element 
# #         if counter > maxCounter:
# #             maxCounter = counter
# #         counter = 0

# # # if counter > maxCounter:
# # #     maxCounter = counter
    
# # print(maxCounter)





# # #lists
# # #operations: adding to front+back/ deleting from front+back, getting elements, replacing 
# # list = [2, 1, 4, 9]
# # list.append(5) #adds to the end of the list; O(1) (could be 0(n) if fixed size array and we need to allocate more memory)
# # list.insert(0, 4)
# # list.pop() #removes from end of list 
# # list.pop(0)
# # print(list[0])
# # print(list)


# #get consectuve ones


# # nums = [1,1,0,1,1,1]



# # def findMaxConsecutiveOnes(nums):
        
# #     counter = 0
# #     maxCounter = 0

# #     for x in range(0, len(nums)):
# #         if nums[x] == 1:
# #             counter+=1 
# #         if nums[x] == 0 or x == len(nums)-1: #if we are at the end of the list 
# #             if counter > maxCounter:
# #                 maxCounter = counter
# #             counter = 0
    
# #     return maxCounter
    
# # print(findMaxConsecutiveOnes(nums))


# #print the number of elements in the list that have even number of digits

# # list2 = [12,345,2,6,7896]

# # countEvenDigits = 0

# # for x in range(0, len(list2)):
# #     #now with each element we want to add to the counter IF the number of digits is even
# #     #easy algo for counting digits 
# #     numDigits = 0
# #     number = list2[x]
# #     while(number != 0):
# #         numDigits+=1 
# #         number = number // 10 #taking a digit out

    
# #     if numDigits % 2 == 0:
# #         countEvenDigits+=1
        

# # print(countEvenDigits) #should we make the calculation even shorter?
# '''   
# #modulus comfortable!
# - divisibility: if x % y == 0 then it means the y can divide into x evenly and so the remainder is 0
# - extracting the right most digit:
#     number % 10 = right most digit and you can just 
#     number % 100 = 2 right most digits 

#     it works with base 10 numbers coz each time u / by 10 you are dividing into the 10s and the numbers are left and its like the 1s and 10s and 100s
# '''

# # numDigits = 0
# # breaking = 2565
# # while(breaking != 0):
# #     numDigits+=1
# #     breaking = breaking // 10 #taking a digit out 
    
# # print(numDigits)




# # def findNumbers(nums):
# #     """
# #     :type nums: List[int]
# #     :rtype: int
# #     """
# #     countEvenDigits = 0

# #     for x in range(0, len(nums)):
# #         #now with each element we want to add to the counter IF the number of digits is even
# #         #easy algo for counting digits 
# #         numDigits = 0
# #         number = nums[x]
# #         while(number != 0):
# #             numDigits+=1
# #             number = number // 10 #taking a digit out 
    
# #         if numDigits % 2 == 0:
# #             countEvenDigits+=1;p[;]
    
# #     return countEvenDigits


# # nums = [12,345,2,6,7896]
# # print(findNumbers(nums))

# nums = [-4,-1,0,3,10]

# front = 0
# end = len(nums)-1
# middle = len(nums) // 2
# if middle == 

# for x in range(0, len(nums)):
#     square = nums[x] * nums[x]
#     nums[x] = square
    

# #sorting algorithms!
# #print(nums)

# #ok so the best sorting algorithm is 



# #Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
# #Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

''''

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
 
 
 
 
 
 
 You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
'''

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

# arr = [1,0,2,3,0,4,5,0]

# i = 0
# while i < len(arr):
#     if arr[i] == 0:
#         arr.insert(i+1, 0)
#         arr.pop()
#         i = i + 2
#     else:
#         i = i + 1

# print(arr)      



