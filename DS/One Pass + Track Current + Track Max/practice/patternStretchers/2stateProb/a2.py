#Longest subarray ending at each index that is:
#DEF REDO THIS PROBLEM!

# even-length: length of the longest even-length subarray ending at i
# odd-length: length of the longest odd-length subarray ending at i

# These are just 2 currents!!!!

nums = [1,2,3,4,5,6,7]

oddLen = 0
evenLen = 0

for i in range(len(nums)):
    
    if evenLen + 1 > 1:
        newOdd = evenLen + 1
    else:
        newOdd = 1
    
    
    if oddLen > 0:
        newEven = oddLen + 1
    else:
        newEven = 0
    
    oddLen = newOdd
    evenLen = newEven

    print(f"index {i}: oddLen={oddLen}, evenLen={evenLen}")
