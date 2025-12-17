nums = [1,1,2]

pointer1 = 0  #holds down the 
pointer2 = 1

while pointer2 < len(nums):
    if nums[pointer1] != nums[pointer2]:
        pointer1 +=1
        nums[pointer1] = nums[pointer2]
    
    pointer2 += 1

print(nums[0:pointer1+1]) #+1 coz slicing function second value is not included
