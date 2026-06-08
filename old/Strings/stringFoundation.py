#String basics (indexing, slicing, immutability) + run time + how it works

# !!!!!!!!!!!!!!!! GET RUN TIMES!!!

#What are strings?

'''

they are array of unicode and they are next to each other in memory
each character has a unicode attatched to it

'''

#Are strings immutable?

'''
python strings are not immutable!
Solutions for changing strings

1. simply make a new string each time you wanna mutate string [not recommended if mutating ALOT]
    newString = newString + "a" 

2. make string into array. arrays are mutable. then make array to string [recommended for mutating ALOT]
    1. appending each character to array 
    2. newString = list(string)
'''

# String Operations

'''
- loop through each character
- slice and get parts of string
- 

'''
















#comparion:

string = "chop"
string2 = "chop2"

if string != string2:
    print("hi")
 
#immutable! this not possible
   
# s1 = "Hello World"
# s1[5] = ','
# print(s1)

#how do immutable strings work with concat?
'''
string = "cat"
string2 = "club"
string + string2 = "catclub"

python will allocate space for the entire why is it 0(n^2)???
need help explaining the equation!
'''


#How to solve this problem?


#concatanate:  
string3 = "rufayda"
end = "!"
print(string3 + end) #how does this work? just creating a new string is probs O(n) where n is the size of string 1 and 2

#get the index of the element!!!!!
print(string3.index("f"))  #O(n)

#get substring using slicing! O(n)
print(string3[:2])





string = "hello"
#string[0] = "k"
#print(string[0])

#how do i change the characters in string!!!! you cant

#Two Pointers:
#Using two variables (indexes) to scan a string (or array) from both ends or sides.

# string = "hello"
# left = 0
# right = len(string) - 1

# while left < right:
#     print(string[left])
#     print(string[right])
#     left += 1
#     right -= 1
   
#ASCII + ORD 




#String basics:

'''
- Strings are immutable so you cant do any in place operation on strings 
- strings = arrays but the elements are characters - 'a'
    - slicing is allowed
    - get their length size; how many characters?
    - loop through
    - compare elements (aka characters + ord())
'''

string = "abracadabra"

count = 0

for x in string:
    if x == "a":
        count = count + 1

print(count)


#Two pointers:

string2 = "timothy"
left = 0
right = len(string2)-1
while left < right:
    print(string2[left], string2[right])
    left += 1
    right -= 1
    

#String concat ***fastest:
chars = ['kite ', 'boat ', 'cat']
s = ''.join(chars)  # "abc"
print(s)

#reversing a string:
string4 = "cat"
reversedString = ""
left = 0
right = len(string4)-1

while left < right:
    
    left += 1
    right -= 1
    

#con cat to string by rewriting a = a + "a"
#make string into an array, then append it