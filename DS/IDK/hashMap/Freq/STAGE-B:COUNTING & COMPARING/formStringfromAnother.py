#Can You Form One String From Another?

#other string must include the same letters + frquency too 

s1 = "aabbcc"
s2 = "aabbccc" 

freqDictS1 = {}

for x in s1:
    if x not in freqDictS1:
        freqDictS1[x] = 1
    else:
        freqDictS1[x] = freqDictS1[x] + 1

for i in s2:
    if i in freqDictS1 and freqDictS1[i] > 0:
        freqDictS1[i] = freqDictS1[i] - 1
    else:
        print("False")