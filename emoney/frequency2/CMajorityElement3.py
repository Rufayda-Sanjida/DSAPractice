# Goal: Find the number that appears more than n/2 times.
"""
Example:

Input: [3,2,3]
Output: 3

Hint:
- more than half the length means theres more of that then any other item
- count frequency, return element with highest count.
- we are dealing with finding the frequency of a bunch of items in a list, need to store them in a frequency hashmap

"""

def myFunction(input):

    myFrequencyMap = {}

    for x in input:
        if x not in myFrequencyMap:
            myFrequencyMap[x] = 1
        else:
            myFrequencyMap[x] = myFrequencyMap[x] + 1
    
    #after populating the frequency map, check which item has the highest value (aka frequency)

    largest = 0
    largestItem = 0
    for x in myFrequencyMap:
        if myFrequencyMap[x] > largest:
            largest = myFrequencyMap[x]
            largestItem = x
    
    return largestItem


print(myFunction(["cat", "dog", "cat", "dog", "dog"]))