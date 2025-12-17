#1. concept: 
''' 
sliding window + hashmap = when we scan an array linearly in groups and 
keep track of the stuff in the group in a dictionary so we can know the freq of it and whenever
using the freq we see our group is invalid, we shrink it from the front and extend it from the back
'''

#2. How the pattern works
'''
1. left = 0, dictionary = {}, best = 0
2. go through the array, adding SOMETHING about the characters 
3. each time tho, see if adding that char makes the window invalid
4. if invalid, subtract the freq 
5. now that its valid, how many char is in the valid window?
'''

#3. Use what?
'''
freq list AND window two pointers 
'''

#4. code template
myList = "abcabcbb"
left = 0
freq = {}
best = 0


for x in range(0, len(myList)):
    #1. add right char into dictionary
    if myList[x] not in freq:
        freq[myList[x]] = 1
    else:
        freq[myList[x]] += 1
    
    print(myList[x])

    #2. while loop : shrink if invalid from the front
    #You only check the frequency of the character you just added + shrink if invalid!

    # freq[myList[x]] > 1:

    while freq[myList[x]] > 1:
        freq[myList[left]] = freq[myList[left]] - 1
        left += 1
    
   
    #3. How many characters are in the window thats valid 
    window_size = x - left + 1
    if window_size > best:
        best = window_size
   
    #HOW MANY CHARACTERS ARE VALID? 



