#anagrams: same number letters and same letters
s = "listen"
t = "silent"

if len(s) != len(t):
    print("already false!")

freqDict = {}
for x in s:
    if x not in freqDict:
       freqDict[x] = 1
    else:
        freqDict[x] = freqDict[x] + 1

for x in t:
    if x not in t:
        freqDict[x] = 1
    else:
       freqDict[x] = freqDict[x] - 1 

for char, count in freqDict.items():
    if count > 0:
        print("False")
