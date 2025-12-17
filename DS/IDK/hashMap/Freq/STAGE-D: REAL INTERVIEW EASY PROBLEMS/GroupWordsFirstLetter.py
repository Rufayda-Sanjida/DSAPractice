myList = ["apple","ant","ball","bat","cow"]

myDictionary = {}

for x in myList:
    if x[0] not in myDictionary:
        myDictionary[x[0]] = [x]
    else:
        myDictionary[x[0]].append(x)

print(myDictionary)