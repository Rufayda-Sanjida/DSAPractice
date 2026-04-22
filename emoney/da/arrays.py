myList = [1, 2, 3, 4, 5]

for x in range(0, len(myList)): #O(n)
    print(myList[x]) 

# accessing element:
print(myList[0])
#run time is big O(1)

myList.append(355)
print(f"the list is {myList} ") #

len(myList) #Amortized O(1) - having space to insert at the end instead of making space 