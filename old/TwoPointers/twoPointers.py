'''
- what is it? two pointers keep track of opposites moving closer together but never collide! stops before collision

- Use cases:
    - keep track of two pointers that move closer to each other and do something each round with the focused pair

- things to remember:
    - when number of elements is odd, the middle element is not seen (coz of the pointer1<pointer2)
'''


#concept: coming from different ends

list = [5, 4, 3, 2, 1]

pointer1 = 0
pointer2 = len(list)-1

print(list[pointer1])
print(list[pointer2])

while pointer1 < pointer2:
    print(f"pointer 1: {list[pointer1]}")
    print(f"pointer 2: {list[pointer2]}")
    print()
    pointer1+=1 
    pointer2-=1


#concept: fast slow method: remove duplicates
num = [1, 2, 2, 3, 4, 4, 5]
print(num)

slow = 1

for x in range(1, len(num)): #the reason why len(nums) is this so we can go through ALL the values!!
    if num[x] != num[x-1]:
        num[slow] = num[x]
        slow = slow + 1

print(num[0:slow])


#theres two types of two pointers algorithms:
#- two pointers coming from opposite directions and never surpassing each other and then the two opposite ends are used for stuff like swapping
#- two pointers: 1 is holding on to the first list, the other one is going and looking for something to replace

