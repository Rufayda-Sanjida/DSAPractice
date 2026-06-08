# 560. Subarray Sum Equals K

array = [1, 2, 3, 4, 5, 6]


k = 5 
count = 0 
for x in range(0, len(array)):  # 0 .. 5 O(n)
    for j in range(x, len(array)): # O(n) 
        
        print(array[x:j+1])  # range of values
        
        sum = 0 
        
        for index in range(x, j + 1):
            sum = sum + array[index]
        
        if sum == k:
            count += 1
        
        print(sum)
    
print(count)

# O(n) 


'''
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 3, 4]
    [1, 2, 3, 4, 5]
    [1, 2, 3, 4, 5, 6]
    [2]
    [2, 3]
    [2, 3, 4]
    [2, 3, 4, 5]
    [2, 3, 4, 5, 6]
    [3]
    [3, 4]
    [3, 4, 5]
    [3, 4, 5, 6]
    [4]
    [4, 5]
    [4, 5, 6]
    [5]
    [5, 6]
    [6]

'''
