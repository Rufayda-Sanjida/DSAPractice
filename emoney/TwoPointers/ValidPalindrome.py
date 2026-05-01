'''

- valid palindrome is seeing if a word or sentance is the same forwards and backwards
    - MOM
    - Rotator
    - Rador

- why is this a two pointers:
    - it helps that we must compare two points at a time comparing the front and end until we get to the middle 
'''

string = "MOM"
front = 0
end = len(string)-1 
while front < end:
    if string[front] != string[end]: 
        print("We end here")
        break
    front = front + 1
    end = end - 1
    