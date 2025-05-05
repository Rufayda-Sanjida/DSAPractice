# def bubbleSort(array):
#     swapped = False
#     for i in range(len(array)-1, 0, -1):
#         for lastElement in range(0, i): #same thing as range(i)
#             if array[lastElement] > array[lastElement+1]:
                
#                 temp = array[lastElement]     # Store array[lastElement] in a temporary variable
#                 array[lastElement] = array[lastElement+1]  # Assign array[lastElement+1] to array[lastElement]
#                 array[lastElement+1] = temp   # Assign temp (original array[lastElement]) to array[lastElement+1]
#                 swapped = True
                
#         if swapped == True:
#             swapped = False
#         else:
#             break
#     return array


# array = [5, 4, 3, 2, 1] #worst case:
# print(bubbleSort(array))


# def selectionSort(array):
#     for x in range(0, len(array)-1): #covers all of the elements 
#         min_idx = x
#         for lastElement in range(x + 1, len(array)):
#             if array[lastElement] < array[min_idx]:
#                 min_idx = lastElement
#         array[x], array[min_idx] = array[min_idx], array[x]
#     return array


# array = [3, 2, 3] #worst case:
# print(selectionSort(array))



# def insertionSort(array):
#     for i in range(1, len(array)):
#         key = array[i]
#         lastElement = i-1
#         while array[lastElement] > key and lastElement >= 0:
#             array[lastElement+1] = array[lastElement]
#             lastElement -= 1
#         array[lastElement+1] = key
#     return array

# array = [5, 4, 3, 2, 1]
# print(insertionSort(array))



# arr =    [1,0,2,3,0,4,5,0]
# newArray = []

# for x in range(0, len(arr)):
#     if len(arr) > len(newArray):
#         newArray.append(arr[x])
#     if arr[x] == 0 and len(arr) > len(newArray):
#         newArray.append(arr[x])
        
# print(newArray)   

#DO IT IN PLACE!

arr =    [1,0,2,3,0,4,5,0]

i = 0
while i < len(arr):
    if arr[i] == 0:
        arr.insert(i+1, 0)
        arr.pop()
        i = i + 2
    i = i + 1

print(arr)






#sorting:

#bubble sort:

# each time you compare 2 elements and move the largest element to the back and you keep sectioning out the largest or smallest 
# the smallest or biggest bubbles to the back

#selectionSort:
#you have a sorted in the beginning and you FIND OR SELECT the next largest or smallest and swap with the first unsorted portion until the very last element who never got swapped stays coz everyone in the beginning got swapped
#worst case = best case scenerio:

#insertionSort: 
#the beginning is the sorted element and for each element you compare with everyone in list and insert it inside 


#sorting algos:
#bubble sort is when you compare pairs and move the smallest to the end and lock it in
#and each round you must decrease the outer loop so that the last sorted positions are locke in fr
#O(n^2)

#insertionSort:
#you have sorted list in the beginning and you insert where it where it fits (could be n)

#selection sort:
#you go through the unsorted part and put it in the beginning like smallest to the front and now its sorted. you swap the first unsorted with the element you found to be the smallest and select and swap: best = worst case