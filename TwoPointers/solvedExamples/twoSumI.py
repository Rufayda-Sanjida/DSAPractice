'''
Goal: you are given SORTED array and a target and you need to return two indices of two numbers that addd up to the target
logic is: if the target is bigger then the front moves up one and if the target is smaller the ending decreases and once the loop ends and it doesn't exit then none
Why is this problem Two pointers? i need to keep track of pointers that are moving closer to each other (heart of two pointers) and we need to have this sorted!! so the comparision part works
'''

list = [1, 2, 3, 4, 5]
target = 3

front = 0
end = len(list)-1

while front < end:
    potential = list[front] + list[end] 
    if potential == target:
        print(list[front], list[end])
        print(front, end)
        break
    elif target < potential:
        end = end - 1
    else:
        front = front + 1

