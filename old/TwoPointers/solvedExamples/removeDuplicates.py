'''
Goal: find the number of unique elements in a sorted list that contains duplicates (so the duplicates are right next to each other)
logic: We loop through with one pointer finding the first occurence of each number (aka unique value) and once we find it, we make it equal to the pointer slow is standing and increment. Slow will be keeping track of the unique elements only moving forward whenever its replaced.
why use? 
- sorted array
- 2 pointers where 1 moves fast (finding unique values) and the other moves slow (keeps track of new orgaanized list) this only works because we are NOT swapping but simply replacing the value of slow and the fast[n-1] is the same and can be accurately compared. 
'''
def removeDuplicates(nums):
    
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[fast - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow

nums = [1, 2, 2, 2, 3, 4, 4]
removeDuplicates(nums)
print(nums)


# [1, 2, 2, 2, 3, 4, 4]
# slow = (starts at second index) 2
# fast = starts at second index = 2 
# We compare fast with fast [n-1] *******
#IF DIFFERENT THEN WE SWAP! if same we dont switch 
#  swap? only time we increase the slow else ALWAYS fast is incrementing!

#1. (iteration) slow = 2 and fast = 2 and fast-1 = 1 (index 3)
    #swap since fast and fast-1 are different!
    # except makes no difference since both fast = slow in the beginning
    #slow++

#2. (2nd iteration) slow = 2 and fast = 2 and fast-1 = 2 (index 3)
    #no swap

#3 (3rd iteration) slow = 2 and fast = 3 and fast-1 = 2 (index 4)
    # 
    #understand by this point that we simply check the number previous to fast to see if its unique and if its unique not matching the previous then we can add it but we leave it alone if its the same since we dont swap but