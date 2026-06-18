
# this doesnt feel like second nature to me


nums = [1, 2, 3, 4]


nums = [1,5,4,2,9,9,9]
k = 3

for x in range(0, len(nums)-k+1):
    for j in range(x + 1, x+k+1): #needs to be one extra coz its NOT includeddddd
        print(nums[x:j])


print()

nums2 = [1,5,4,2,9,9,9]
k2 = 3
print("better here: ")

for p in range(0, len(nums2)-k2+1): #stopping before we go over the last 3
    workingSubarray = nums2[p:p+k2]
    print(workingSubarray)



'''
BOTH SAME SLICING PLACES BUT THE DIFFERENCE IS:

I WANT BOTH TO BECOME X + K EXCEPT WHEN IM DOING RANGE -> CUTS TOO EARLY SO THE SLICE CAN NEVER REACH SLICE[X:X+K]
COZ RANGE CUTS IT OFF EARLY!!!!


- ANOTHER RULE OF THUMB:

for x in range(0, len(nums)-k+1):
    for j in range(x + 1, x+k+1):
        print(nums[x:j])

        #### REMEMBER ### 
        - j is simply the ending where should i end??? x stays consistant
        


'''
