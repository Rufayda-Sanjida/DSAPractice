
nums = [1,5,4,2,9,9,9]
k = 3

for p in range(0, len(nums)-k+1): #stopping before we go over the last 3
    workingSubarray = nums[p:p+k]
    print(workingSubarray)



'''
sliding window:

- enlarge window
- shrink if needed -> while statement
- calculate information 

'''