
s = "A man, a plan, a canal: Panama"

def ValidPalindrome(s):
    beginning = 0
    end = len(s)-1

    while beginning < end:
        while s[beginning].isalnum() == False:
            beginning = beginning + 1
        
        while s[end].isalnum() == False:
            end = end - 1
        
        last = s[end].lower()
        first = s[beginning].lower() 
        
        if last != first:
            return "not a palindrome"
        else:
            beginning = beginning + 1
            end = end - 1
    
    return "a palindrome!"

print(ValidPalindrome(s))