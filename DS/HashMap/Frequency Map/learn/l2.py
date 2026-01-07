'''
Example 2: LC 242 — Valid Anagram

Question:
Do two strings have the same character frequencies?


anagrams = can you use these given alphabets rearrange and make both given strings: basically each string we must store how many shows up

Explanation

Count characters in s

Count characters in t

Compare maps

'''

string1 = "cat"
string2 = "tacc"


hashmap1 = {}
hashmap2 = {}

if len(string1) != len(string2):
    print("not an anagram")


#lets store the frequency of the letters that show up 
for x in range(len(string1)):
    if string1[x] not in hashmap1:
        hashmap1[string1[x]] = 1
    else:
        hashmap1[string1[x]] += 1
    
    if string2[x] not in hashmap2:
        hashmap2[string2[x]] = 1
    else:
        hashmap2[string2[x]] += 1

for key in hashmap1:
    if key not in hashmap2:
        print("not an anagram")
    else:
        if hashmap1[key] != hashmap2[key]:
            print("not an anagram")
            break
   
    # if hashmap1[key] != hashmap2[key]:
    #     print("not anagram")


