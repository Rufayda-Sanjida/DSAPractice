'''
ok so basically:
i am trying to remove characters from a string until there are no more characters left
i have to say how many steps it took to get to 0 characters
1 twist = palindromic parts are considered 1 move as you can get rid of them all in 1 move
- the palindrome subsequence doesn't need to be completely perfect they can be in different parts of the string -not contingent

input = a string
output = number - how many steps it took to get to get rid of all characters

method 1 = go through the string with 2 pointers SEARCHING for palindromes
then remove them 1 one step and set counter ++ 
then length of the remaining string is all 1 move so 1 + remaining string length 
'''


def removePalindromicSubsequence(s):
    s = list(s) #converting to list because strings are not mutable!

    beginning = 0 #index of 1st element
    ending = len(s)-1 #index of last element
    palindromeRemoved = False
    count = 0

    #one move for finding palindromes:
    while beginning < ending:
        #assume all as and bs and lowercase
        
        while s[beginning] != s[ending]:
            ending = ending - 1

        #remove the palindrome 
        if s[beginning] == s[ending]:

            s.pop(ending)
            s.pop(beginning)
            ending = ending - 1
            palindromeRemoved = True

    #by now we hope the palindromes in their crazy places have been removed 
    if palindromeRemoved == True:
        count = count + 1

    count = count + len(s)
    return (count)

s = "baabb"
print(removePalindromicSubsequence(s))