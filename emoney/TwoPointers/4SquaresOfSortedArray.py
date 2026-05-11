'''
- sorted squares, 

- why is this two pointers?
    - because the largest numbers come from the ends and so we just need to really compare the ends 

'''

numbers = [-12, -4, -1, 0, 3, 10]

#method 1: just sort it by getting the positives of the numbers 

#method 2: two pointers
front = 0
end = len(numbers) - 1

while front != end: 
    squaredFront = numbers[front] * numbers[front]
    squaredEnd = numbers[end] * numbers[end]
    if squaredFront > squaredEnd:
        #Swap
        holder = numbers[end]
        numbers[end] = numbers[front]
        numbers[front] = holder
    numbers[end] = numbers[end] * numbers[end]
    end = end - 1

numbers[front] = numbers[front] * numbers[front]
print(numbers)
