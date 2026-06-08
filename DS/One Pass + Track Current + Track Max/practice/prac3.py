#Longest strictly decreasing subarray


longestDecreasing = 1
num = [3, 2, 1, 5, 4, 3, 1, 0]
currentNum = 1


for x in range(1, len(num)):
    if num[x-1] > num[x]:
       currentNum = currentNum + 1
    else:
        currentNum = 1

    if longestDecreasing < currentNum:
        longestDecreasing = currentNum


print(longestDecreasing)

    
