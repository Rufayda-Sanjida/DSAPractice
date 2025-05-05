'''
Given an array nums of integers, return how many of them contain an even number of digits.

Example 1:

Input: nums = [12, 345, 2, 6, 7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
Example 2:

Input: nums = [555,901,482,1771]
Output: 1 
Explanation: 
Only 1771 contains an even number of digits.
 
'''

listNum = [555, 901,482,1771]
evenDigit = 0
for x in range(0, len(listNum)):
    
    while listNum[x] > 0:
        
    
        count += 1



nums = []
countEvenDigits = 0

for x in range(0, len(nums)):
    #now with each element we want to add to the counter IF the number of digits is even
    #easy algo for counting digits 
    numDigits = 0
    number = nums[x]
    while(number != 0):
        numDigits+=1
        number = number // 10 #taking a digit out 

    if numDigits % 2 == 0:
        countEvenDigits+=1
        
print(countEvenDigits) 

# 221 % 10 = 1 (how to get the last digit) easy modulus just gives you the remainder when you divide the number evenly into 10s, you'll always get the digit left over if not evenly divide into 10
# 221 // 10 = 22 (how to get rid of the last digit) ?? a bit more harder to understand!!!