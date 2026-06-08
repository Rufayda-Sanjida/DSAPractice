
nums = [1, 2, 3, 4]

for x in range(0, len(nums)):
    for j in range(0, 5):
        # j loop range never becomes invalid so for each nums -> it will loop 5 times
        print(x, j)


array1 = [1, 2, 3, 4]
for q in range(0, len(array1)):  # len(array1) = 4 & last index = len(array) - 1
    for w in range(q + 1, len(array1)):
        '''
        HOW TO GET UNIQUE COMBINATIONS 
        1. q = 3 (ending is 4)
           w = 4 (ending is 4) -> range (4, 4) = invalid range
        2. you can save a loop = end the top loop by doing len(nums) - 1 since the bottom will increase to get the second to last index ->  last index is not needed

        '''
        print(x, w)

array2 = [2, 4, 6, 8]
for i in range(0, len(array2)): 
    for p in range(i + 1, len(array2) + 1):
        
        # i ending at len(nums) AND p ending at len(nums) = p goes up by 1 but since they end at the same place
        # last number is NOT excuted by p since -> 
        '''
        1. since p (i + 1) is moving closer to end -> range DOES become invalid eventually
        2. if both loops at the same place at len(nums) 
            - the second part WILL NOT run since the range becomes invalid if increased 
        3. this is how to get the LAST index as well
        4. good for subarrays 
        '''

        print(nums[i]) #VALID 





nums = [1,2,3,4,5,6]


for i in range(0, len(nums)): 
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j]) #VALID


for i in range(0, len(nums)+1): 
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j]) #VALID


for i in range(0, len(nums)+300): 
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j]) # ALSO VALID


'''
inner loop becomes -> range(i+1, len(nums))
len(nums) = not changing BOUNDED
i + 1 = gets hugeeee

but range function: 


'''



'''
Loop 1

i = 2  ; nums[2] = 3 -> range (0, 4) -> 1, 2, 3, 4
j = 3  ; nums[3] = 4 -> range (3, 4) VALID

i = 3
j = 4 -> range (4, 4) = invalid 

orrrr

i = 3
j = 4 -> range(4, 4+1=5) => making the last one included 


'''
''''
for x in range(0, len(nums)+1):
    for j in range(0,1):
        print(nums[x], nums[j])

'''