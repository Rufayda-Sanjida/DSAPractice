'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not). 

Example 1: 
Input: s = "abc", t = "ahbgdc"
Output: true

'''

#hint: slow/fast two pointers
string = "ahbgdc" #fast
substring = "abc" #slow
#substrings is a new string thats formed from original string by deleting some or nonewithout disturbing relative positions the remaining characters

#ok idea: slow keeps track of the substring we are looking for and fast goes through the string and each time it finds something from slow, it increments the slow until it should stop early if all of the substring stuff is stopped

slow = 0

for fast in range(0, len(string)):
    if string[fast] == substring[slow]:
        slow = slow + 1
    if slow == len(substring): #SO ACTUALLY WE AREGONNA STOP BEFORE
        print("YOU WIN")
        break
    





