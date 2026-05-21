# Majority Element
nums = [2,2,1,1,1,2,2]

dictionary = {}

for x in nums:
    if x not in dictionary:
        dictionary[x] = 1
    else:
        dictionary[x] += 1 

largest = 0
largestElement = 0
for x in dictionary:
    if dictionary[x] > largest:
        largest = dictionary[x]
        largestElement = x

print(largestElement, largest)


def majorityElement(nums):
    dictionary = {}

    for x in nums:
        if x not in dictionary:
            dictionary[x] = 1
        else:
            dictionary[x] += 1 

    largest = 0
    largestElement = 0
    for x in dictionary:
        if dictionary[x] > largest:
            largest = dictionary[x]
            largestElement = x

    #print(largestElement, largest)
    return largestElement


#brute force
def majorityElement(nums):
        majority_count = len(nums) // 2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

majorityElement([2,2,1,1,1,2,2])