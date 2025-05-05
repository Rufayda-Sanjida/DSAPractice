def merge(left, right):
    result = []
    i,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2: #when there is only 1 element in list
        return list
    middle = len(list) // 2
    
    left = mergesort(list[0:middle])
    right = mergesort(list[middle:])
    return merge(left, right)


num = [5, 4, 2, 1]
print(mergesort(num))
'''

How does merge sort work?

num = [5, 4, 2, 1]
1. cut it in half and send it back to function
left = mergesort([5, 4]) -- --------------------------
2. cut it up half again and send it back to function 
left = mergesort([5])
3. now theres only 1 element in the list, it returns 
left = [5] 
4. pick up from 1 where we got left side of 
list mergesort([5, 4]) left side=[5] and right side=mergesort([4])
5. rightside = mergesort([4]) = returns rightside = [4]
6. so far we got:
leftside = [5]
rightside = [4]
merge(left [5], right [4]) -> merging works by comparing the firsts of lists as they are the littest and so on until no more to compare and the rest of whatever list is left is appended to the end of result
7. left = mergesort([5, 4]) = returned [4, 5]
8. right = mergetsort([2, 1]) 
9. left = mergesort([2]) 
10. left = [2]
11. right = mergesort([1])
12. right = [1]
13. left = [2] and right = [1]
14. merge(left [2], right [1])
15. merge will take the first indexes of both and compare to see who is smaller since both first indices are the smallest of both so comparing the first is enough
16. merge(left [2], right [1]) = [1, 2]
17. right = [1, 2]
18. left = [4, 5]
19. right = [1, 2]
20. merge(left [4, 5], right [1, 2])
21. left and right lists the first indices are compared and incremented and one list will be left with unsorted elements in the big list and those will all be appended to the list
22. merge(left [4, 5], right [1, 2]) = [1, 2, 4, 5]

'''


def mergesort(list):
    if len(list) < 2:
        return list
    
    middle = len(list) // 2
    
    left = mergesort(list[0:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0 #left
    j = 0 #right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    #after while loop is over:
    result = result + left[i:]
    result = result + right[j:]
    return result
  
  
  
def mergesort(list):
    if len(list) < 2:
        return list
    
    middle = len(list) // 2
    
    left = mergesort(list[0:middle])
    right = mergesort(list[middle:])
    return merge(left, right)  

def merge(left, right):
    result = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    #once im done my loop: append rest of the list
    result = result + left[i:]
    result = result + right[j:]
    return result 



def mergesort(array):
    
    if len(array) < 2:
        return array
    
    middle = len(array) // 2
    left = mergesort(array[0:middle])
    right = mergesort(array[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result = result + left[i:]
    result = result + right[j:]
    return result