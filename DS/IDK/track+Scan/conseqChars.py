#2. LC 1446 – Consecutive Characters

s = "leetcode"

if len(s) == 1:
    print(1)

largest = 0

count = 0

for x in range(0, len(s)-1):

    if s[x] == s[x+1]:
        count = count + 1
    else:
        count = 0
    
    if largest < count:
        largest = count
    
