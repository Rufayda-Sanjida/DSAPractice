myList = "abcabcbb"
left = 0
freq = {}
best = 0


for right in range(len(myList)):
    c = myList[right]
    
    # add right char
    freq[c] = freq.get(c, 0) + 1
    
    # shrink while invalid
    # invalid means CURRENT char count > 1
    while freq[c] > 1:
        freq[myList[left]] -= 1
        left += 1

    # update best
    best = max(best, right - left + 1)

print(best)
