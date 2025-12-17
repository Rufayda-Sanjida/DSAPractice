
myList = [3,2,3]
countDict = {}

for x in myList:
    if x not in countDict:
        countDict[x] = 1
    else:
        countDict[x] = countDict[x] + 1

for num, count in countDict.items():
    if count > len(myList)/2:
        print(f"{num} - {count}")
        break
