'''
- the array with characters reversed in place—meaning the original array is modified directly, without creating an additional copy. 
    - hello -> olleh

- Why is this two pointers?
    - to reverse a string, i simply need to take both sides and replace it with each other
    - so i need two pointers from both sides
'''

String = "hello"
myList = []
for x in String:
    myList.append(x)

print(myList)

front = 0
end = len(myList) - 1

while front < end:
    #Swap
    holder = myList[front]
    myList[front] = myList[end]
    myList[end] = holder
    front = front + 1 
    end = end - 1

print(myList)