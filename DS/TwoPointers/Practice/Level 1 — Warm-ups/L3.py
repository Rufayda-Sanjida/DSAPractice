#3️⃣ Count how many unique elements exist

'''
many unique elements exist?
Version A (most common in interviews)

Input type:

❌ NOT sorted
Arbitrary list -> hashmap girl


✅ SORTED 
Duplicates are adjacent

'''

nums = [1, 1, 2, 2, 3, 4, 4, 5, 6, 6]

pointer1 = 0

for x in range(1, len(nums)):
    if nums[x-1] != nums[x]:
        pointer1 = pointer1 + 1
        nums[pointer1] = nums[x] #no swapping only because we need that element to be there


print(nums[0:pointer1+1])