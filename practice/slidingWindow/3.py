## 3. Longest Substring Without Repeating Characters


'''
Given a string s, find the length of the longest substring without duplicate characters.

- substring = subarray

'''


string = "abcabcbb"
front = 0

maxLength = 0

frequenceMap = {}

for end in range(0, len(string)):

    # 1. is end in frequency map: (a duplicate)
        # no -> 
            #  add end to frequency map
            # update current length of unique numbers from front to end
        # yes -> 
            # do these until frequency[front] not in map anymore
                # decrease frequency[front] + delete key if value = 0
                # increase front 
            # add end to frequencyMap
    
    
    while string[end] in frequenceMap:
        frequenceMap[string[front]] -= 1
        if frequenceMap[string[front]] == 0:
            del frequenceMap[string[front]]
        
        front += 1
        
    frequenceMap[string[end]] = 1
    maxLength = max(maxLength, len(string[front:end]) + 1)
    



print(maxLength)


# # brute force:
# s = "abcda"
# maxLength = 0

# for x in range(0, len(s)):
#     frequencyMap = {}
#     count = 1
#     frequencyMap[s[x]] = 1

#     for j in range(x + 1, len(s)):
#         if s[j] not in frequencyMap:
#             frequencyMap[s[j]] = 1
#             count = count + 1
#         else:
#             break

#     if count > maxLength:
#         maxLength = count       
#         # keep iterating in the array until you find it in the hashmap: break
#         # save length + compare + replace if necessary
#     #print(s[x:j])
    
# print(maxLength)
    