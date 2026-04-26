''''

nums = [1,1,1]
k = 2
Output: 2

'''

def SubArraySum(array, targetSum):

    listOfSolutions = []
    runningSumHashmap = {}

    currentSum = 0
    for x in range(0, len(array)):
       
        # 1. GET current sum: add to running sum:
        currentSum = currentSum + array[x]
        
        # array = [1, 2, 3]
        # runningSumHashmap = {1: 0, 3: 1, 6: 2}

        # 2. Can we find a prefix sum we can get rid of to get our target?
        prefixSumWeCanGetRidOf = currentSum - targetSum

        # 3. check if it exists
        if prefixSumWeCanGetRidOf in runningSumHashmap:
            # we found a prefix sum we can get rid of from the begginning to get our desired sum
            # lets add every number from that prefix sum to current! to a list
            listOfSolutions.append(array[  runningSumHashmap[prefixSumWeCanGetRidOf] + 1   : x+1] )


            '''
            
            
            listOfSolutions.append(array[  runningSumHashmap[prefixSumWeCanGetRidOf] + 1   : x+1] )
            since runningSumHashmap[prefixSumWeCanGetRidOf]  is the index of the prefix sum we just add 1 to get everything after wards right?

            runningSumHashmap[...] gives you the index where the prefix sum ended

But that prefix sum includes everything up to that index.

So the subarray you want starts after that index.

and slicing second argument is not included so you gotta go up 1 to include the current!!!!

            '''

        runningSumHashmap[currentSum] = x
    return listOfSolutions



print(SubArraySum([1, 2, 3], 5))



# You might accidentally use the current prefix sum as the one you’re trying to remove.
'''
you cant get rid 

ou might accidentally use the current prefix sum as the one you’re trying to remove.
how can this be if we are calculating the prefix sum by subtracting from the currentSum the current cant be the prefix sum 


OHHH OK SO I CANNOT PUT THE CURRENT ON COZ IT COULD HONESTLY EQUAL IT IF OUR TARGET IS 0?

currentSum = 2
store 2 in hashmap

need = 2 - 0 = 2
'''



''''

2️⃣ Why do we need {0: -1}?

This is to handle subarrays that start at index 0.

Example
nums = [1, 2, 3]
k = 3

We want [1,2].

At index 1:

currentSum = 3
need = 3 - 3 = 0

We ask:

👉 “Have we seen prefix sum = 0?”

If we DIDN’T put {0: -1}, answer is ❌ no → we miss [1,2]

this is only when we have to get everything from the whole list 
'''