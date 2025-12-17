#Return the count of each word.
stringsList = ["apple", "banana", "apple", "apple", "banana", "cherry"]
countDict = {}

for x in stringsList:
    if x not in countDict:
        countDict[x] = 1
    else:
        countDict[x] = countDict[x] + 1

print(countDict)