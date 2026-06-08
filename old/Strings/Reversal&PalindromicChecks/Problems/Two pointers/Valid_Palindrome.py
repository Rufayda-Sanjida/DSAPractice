# #this is a palindrome because: after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.
# #so i can simply check if the ends match and go forward or backwards


# # #how to convert string to uppercase? lowercase?
# # #what ascii is ONLY alphabet so i can avoid the non-alphanumeric characters?

def validPalindrome(s): #O(n/2)

    left = 0
    right = len(s)-1

    while left < right:
        #check if s[left] is alphabet and if its not left ++
        # if not(64 < ord(s[left]) < 91) and not(96 < ord(s[left]) < 123):
        #     left = left + 1
        
        while not(64 < ord(s[left]) < 91) and not(96 < ord(s[left]) < 123):
            left = left + 1
        
        #check if s[right] is alphabet and if not right --
        while not(64 < ord(s[right]) < 91) and not(96 < ord(s[right]) < 123):
            right = right - 1 
        
        #then when both are letts  #make s[left] and s[right] lowercase
        num = ord(s[left])
        num2 = ord(s[right])
        
        if not(96 < ord(s[left]) < 123):
            num = num + 32
        
        if not(96 < ord(s[right]) < 123):
            num2 = num2 + 32
        
        #then check this condition!
        if num != num2:
            # print("Not a palindrome!")
            # break
            return ("Not a Palindrome")
        
        left = left + 1
        right = right - 1 
        
    return ("Its A Palindrome")
    
s = "A man, a plan, a canal: Panama"
print(validPalindrome(s))


#Ok so this algorithm is where i start from the front and back and hopefuly meet in the middle but since not all elements are valid characters
#best case = O(n/2) and worse case O(n) if theres bunch of nonsense characters