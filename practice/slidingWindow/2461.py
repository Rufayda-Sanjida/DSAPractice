# 2461. Maximum Sum of Distinct Subarrays With Length K

'''

integerArray = [1, 2, 3, 4]
integerK = k (length of subarray)

- find all length 3 subarrays from array
- ask if those elements in the subarray are distinct??
    - if distinct ? find sum
        - if sum greater than largestSum seen so far -> replace sum
    - if not distinct -> next subarray

    
lesson learned:

nested loops = if i only want the subarray that goes up to a certain length each time??


for x in range(0, len(nums)-k+1): 
    for j in range(x + 1, x+3+1):
        print(nums[x:j])

- now this will give us only 3 subarrays at a time
- top must stop 3 away so we can get the last 3 BUT + 1 coz not included
    


for x in range(0, len(nums)-k+1):
    for j in range(x + 1, x+k+1): #needs to be one extra coz its NOT includeddddd
        
        print(nums[x:j])
        # we dont even need to reiterate with a loop here since are are just looking for subsets
        
'''

# largestSum = 0

# for x in range(0, len(nums)-k+1):
#     for j in range(x + 1, x+k+1): #needs to be one extra coz its NOT includeddddd
        
#         print(nums[x:j])
        # we dont even need to reiterate with a loop here since are are just looking for subsets
        
        # are those elements in nums[x:j] distinct????
        
        #hashmap of what ive seen before -> if ive seen it? exit loop
        # seenBefore = False
        # hashmap = {}
        # for i in nums[x:j]:
        #     if i not in hashmap:
        #         hashmap[i] = 1
        #     else:
        #         seenBefore = True
        #         break
        
        # #if distinct -> get the sum
        # mySum = 0
        # if seenBefore == False:
        #     for p in nums[x:j]:
        #         mySum = mySum + p
        
        # if mySum > largestSum:
        #     largestSum = mySum

        
#print(largestSum)

# or 
'''

nums = [1,5,4,2,9,9,9]
k = 3
for x in range(0, len(nums)):
    for j in range(x, len(nums)):
         print(nums[x:j+1])

'''



'''

nums = [1,5,4,2,9,9,9]
k = 3
largestSum = 0
print("better here: ")

for p in range(0, len(nums)-k+1): #stopping before we go over the last 3
    workingSubarray = nums[p:p+k]
    print(workingSubarray)
     
    # 1. are those elements in nums[x:j] distinct????
        
    #hashmap of what ive seen before -> if ive seen it? exit loop
    seenBefore = False
    hashmap = {}
    for i in workingSubarray:
        if i not in hashmap:
            hashmap[i] = 1
        else:
            seenBefore = True
            break
    
    # 2. if distinct -> get the sum
    mySum = 0
    if seenBefore == False:
        for x in workingSubarray:
            mySum = mySum + x
    
    if mySum > largestSum:
        largestSum = mySum

print(largestSum)

'''

nums = [1,5,4,2,9,9,9]
k = 3


largestSum = 0
currentSum = 0
countDictionary = {}

front = 0

for back in range(0, len(nums)):
    
    # expand window: include nums[back]
    val = nums[back]
    currentSum = currentSum + nums[back]

    if val not in countDictionary:
        countDictionary[val] = 1
    else:
        countDictionary[val] = countDictionary[val] + 1
    
    # 2. shrink window while it is invalid
    # invalid means:
    # - window is bigger than k
    # - OR nums[back] caused a duplicate
    while (back - front + 1 > k):
        countDictionary[nums[front]] -= 1
        currentSum -= nums[front]

        if countDictionary[nums[front]] == 0:
            del countDictionary[nums[front]]
        
        front += 1
    
    # 3. now window is valid
    # if it has exact length k, AND no duplicates:
    if back - front + 1 == k and len(countDictionary) == k:
        largestSum = max(largestSum, currentSum)

'''
window size is back - front + 1
'''