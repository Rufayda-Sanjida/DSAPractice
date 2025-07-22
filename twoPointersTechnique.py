list = [1, 2, 3, 4, 5]

left = 0
right = len(list)-1

while left < right:
    print(list[left], list[right])
    left += 1
    right -= 1

#Two pointer technique = 2 pointers from left and right move closer to the middle until the left surpasses the right which is when you stop

#Used for finding pairs = two pointers = two pairs

#two pairs that equal a certain number? [caution the array must be in sequential order]
target = 3
while left < right:
    if (list[left] + list[right] == target):
        print(list[left], list[right])
    elif (list[left] + list[right] < target)
        left += 1
    else:
        right -= 1