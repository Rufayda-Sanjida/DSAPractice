s = ["h","e","l","l","o"]

left = 0
right = len(s)-1

while left < right: #O(n/2)
   #everything here is O(1)
   temp = s[left]
   
   s[left] = s[right]
   s[right] = temp
   
   left = left + 1
   right = right - 1

print(s)