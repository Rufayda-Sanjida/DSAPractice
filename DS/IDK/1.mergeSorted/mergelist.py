#solution 1: insert smaller array into bigger then sort
list1 = [1, 2, 3, 0, 0, 0] #len = m 
list2 = [2, 5, 6] # len = n 

var = 0
for x in range(len(list2), len(list1)):
    list1[x] = list2[var]
    var = var + 1

#above is m + n 

list1.sort()
print(list1)
#above is (m + n) * log (m + n)

#total = m + n + (m + n) * log (m + n))
#CHECK IF CORRECT!
#solution 2: 

list1 = [1, 2, 3, 0, 0, 0] #len = m 
list2 = [2, 5, 6] # len = n 
n = len(list2) #3
m = len(list1)-n #6-3 = 3
newArray = []


pointer1 = 0
pointer2 = 0
pointer3 = 0
while pointer1 < m and pointer2 < n:
    if list1[pointer1] < list2[pointer2]:
        newArray.append(list1[pointer1])
        pointer1 += 1
    else:
        newArray.append(list2[pointer2])
        pointer2 = pointer2 + 1


#must iterate through both only coz of the 0s at the end
while pointer1 < m:
    newArray.append(list1[pointer1])
    pointer1 += 1    

while pointer2 < n:
    newArray.append(list2[pointer2])
    pointer2 += 1     
