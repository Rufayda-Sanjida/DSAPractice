#Max Consecutive Ones II (LC 487) 
#
nums = [1,0,1,1,0]

noFlip = 0
largest = 0
flipOnceStreak = 0
seenZeroBefore = 0

for x in nums:
    if x == 1:
        noFlip += 1
    else:
        noFlip = 0
    
    if x == 1:
        flipOnceStreak += 1
    elif seenZeroBefore == 0 and x == 0:
        flipOnceStreak += 1
        seenZeroBefore += 1
    else:
        flipOnceStreak = 0
        seenZeroBefore = 0

    if largest < noFlip:
        largest = noFlip

    if largest < flipOnceStreak:
        largest = flipOnceStreak

print(largest)