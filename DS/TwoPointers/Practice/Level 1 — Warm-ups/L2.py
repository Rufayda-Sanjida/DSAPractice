#2 Remove all occurrences of a value x

'''
hint: we are being told to remove aka modify the list 
-> same direction two pointers: read and write keep track of every unique 
-> “Remove in place without extra space” 
not sorted! 
'''

nums = [3, 2, 2, 3, 4, 3, 5, 6, 3]
target = 3

pointer1 = 0

for x in range(0, len(nums)):
    if nums[x] != target:
       save = nums[pointer1]
       nums[pointer1] = nums[x]
       nums[x] = nums[pointer1]
       pointer1 = pointer1 + 1

print(nums[0: pointer1])