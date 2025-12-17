string = "aabccc"

freqDict = {}

for x in string:
    if x not in freqDict:
        freqDict[x] = 1
    else:
        freqDict[x] = freqDict[x] + 1

largestChar = None
largestDict = 0
for char, count in freqDict.items():
    if largestDict < count:
        largestDict = count
        largestChar = char

print(f"largest: {largestChar} : {largestDict}")
