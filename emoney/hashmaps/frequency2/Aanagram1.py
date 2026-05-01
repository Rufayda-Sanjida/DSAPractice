#Goal: Return True if two strings contain the same letters with same frequency.
#hint: frequency aka count aka store in hashmap frequency!!

def myFunction(s, t):
    
    # if not the same length, already false!
    if len(s) != len(t):
        return ("Not anagrams!")

    hashmapForS = {}

    for x in s:
        if x not in hashmapForS:
            hashmapForS[x] = 1
        else:
            hashmapForS[x] = hashmapForS[x] + 1

    #print(hashmapForS)

    for letter in t:
        if letter in hashmapForS:
            if hashmapForS[letter] == 0:
                return ("Not anagrams!")
            
            hashmapForS[letter] = hashmapForS[letter] - 1
        else:
            return ("Not anagrams!")
    
    return ("They are anagrams")


#Input: 
s = "listens"
t = "silent"
print(myFunction(s, t))
#Output: True