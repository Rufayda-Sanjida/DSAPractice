list1 = [1, 2, 3, 0, 0, 0] #len = m 
list2 = [2, 5, 6] # len = n 
n = len(list2) #3
m = len(list1)-n #6-3 = 3

pointer1 = m-1
pointer2 = n-1
pointer3 = (m + n)-1 

while pointer1 >= 0 and pointer2 >= 0: 
    if list1[pointer1] > list2[pointer2]:
        list1[pointer3] = list1[pointer1]
        pointer1 -= 1
    else:
        list1[pointer3] = list2[pointer2]
        pointer2 -= 1 
    pointer3 -= 1

while pointer1 >= 0:
    list1[pointer3] = list1[pointer1]
    pointer1 -= 1
    pointer3 -= 1

while pointer2 >= 0:
    list1[pointer3] = list2[pointer2]
    pointer2 -= 1
    pointer3 -= 1

print(list1)