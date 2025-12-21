#167. Two Sum II - Input Array Is Sorted
'''
sorted + add the numbers up = 

if its bigger move forward if its smaller, move inwards

'''
numbers = [2,7,11,15]

target = 9

front = 0
back = len(numbers)-1

while front < back:
    sum = numbers[front] + numbers[back]

    if sum == target:
        #print(front + 1, back + 1)
        break
    elif sum > target:
        back = back - 1
    else:
        front = front + 1


array = []
array.append(front + 1)
array.append(back + 1)
print(array)