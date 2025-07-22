myList = [1, 2, 3, 4, 5]
print(myList)

#end: add + delete
myList.append(6) #0(1) or 0(n)
print(f"appending 6: {myList}" )

myList.pop() #0(1) or 0(n)
print(f"taking out the end 6: {myList}" )

#beginning: add + delete
myList.insert(0, 1) # 0(n)
print(f"inserting to front: {myList}" )

myList.pop(0) # 0(n)
print(f"taking out the front: {myList}" )
