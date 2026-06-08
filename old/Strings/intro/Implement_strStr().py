haystack = "leetcode"

needle = "leeto"

x = 0

while x < len(haystack):
    if haystack[x:len(needle)] == needle:
        print(x)
        break
    x = x + 1
    
