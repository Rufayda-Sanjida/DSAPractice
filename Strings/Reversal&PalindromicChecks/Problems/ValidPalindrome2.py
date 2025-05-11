'''
given a string s, return true if s can be palindrome after deleting 
at most one character from it


input = string
output = true or false

what are we doing to the input: we are trying to see if we can make s into a palindrome after deleting one character`1231```12w
'''

def firstONE(s):
    #removing so need to make to array
    #if not alowed to make to an array => slicing and making a new string - not a bad idea, its better just need to allocate memory TWICE 

    s = list(s)

    beginning = 0
    ending = len(s)-1

    while beginning < ending:
        #assume valid chars ONLY 
        if s[beginning] != s[ending]:
            #when they dont match! #delete one and see if you can keep going, cant? delete the other one and see if you can keep going, cant? not a palindrome
            if palindromeChecker(s[beginning+1:ending+1]) == True: #if the first one works
                return True
            elif palindromeChecker(s[beginning:ending]) == True: 
                return True
            else:
                return False
        
        beginning = beginning + 1
        ending = ending - 1
    return True


#function for going through the list to see if its a palindrome!
def palindromeChecker(s):

    if len(s) <= 2:
        return True
    
    beginning = 0
    ending = len(s)-1

    while beginning < ending:
        #assume valid chars ONLY 
        if s[beginning] != s[ending]:
            return False
        
        beginning = beginning + 1
        ending = ending - 1

    return True


#already a palindrome 
s = "abapwpacba"
print(firstONE(s))


#How would you feel marrying someone who constantly critizes u, keeps reminding you of your mistakes when you desperatly need to move on from it


# [3-7included] = [p, w, p, a, c] = false 
# [2included - 6 inlcuded (7 not included)] = True [a, p, w, p, a]