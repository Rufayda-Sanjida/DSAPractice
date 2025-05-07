def is_valid_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum()) #join each lower case alphabet AND number; need the join coz loop will produce an array of chars and it will be turned in to a string
    return s == s[::-1]
    
