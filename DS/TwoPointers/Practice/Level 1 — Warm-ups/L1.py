#Move all even numbers to the front (keep order)

'''

not sorted
Move all even numbers to the front (keep order)
- we are moving something = modifying the list in place
- same direction; pointer 1 to write and pointer2 to read
'''

numbers = [3, 1, 4, 2, 5, 6]

pointer1 = 0

for x in range(0, len(numbers)):

    if numbers[x] % 2 == 0:
        save = numbers[pointer1]
        numbers[pointer1] = numbers[x]
        numbers[x] = save
        pointer1 = pointer1 + 1
        #if you dont swap, you lose information 

print(numbers)