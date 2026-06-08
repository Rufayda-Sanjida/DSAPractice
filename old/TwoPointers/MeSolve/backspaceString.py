# # s = "ab#c"
# # t = "ad#c"

# s = "ab##"
# t = "c#d#"
# skipCounterS = 0
# skipCounterT = 0

# i  = len(s)-1 #currently on the last index of s
# j = len(t) - 1 #currently on the last index of t

# print(i, j)


# while i > -1 and j > -1:
#     if s[i] == "#":
#         skipCounterS = skipCounterS + 1
#     else:
#         i = i - 1
#     if t[j] == "#":
#        skipCounterT = skipCounterT + 1
#     else:
#        j = j - 1
    
#     if s[i] != t[j]:
#         print("Not the same")
#         break
    
#     print(s[i])
#     print(t[j])

#     # i = i - 1
#     # j = j - 1


s = "ab#c"
t = "ad#c"

i  = len(s)-1 #currently on the last index of s
j = len(t) - 1 #currently on the last index of t

skipCounterS = 0
skipCounterT = 0

while i > -1 and j > -1:
    while s[i] == "#":
        skipCounterS = skipCounterS + 1
        i = i - 1
    else:
        #delete until the skipcounter is 0
        while skipCounterS > 0:
            i = i - 1
    while t[j] == "#":
        skipCounterT = skipCounterT + 1
        j = j - 1
    else:
        while skipCounterT > 0:
            j = j - 1

    #now we should be able to compare stuff!
    if s[i] != t[j]:
        print("YOU LOSE")
        break