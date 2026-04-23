"""
Group Anagrams (important):

Group words with same letter counts.

["eat","tea","tan","ate","nat","bat"]

Output:
[["eat","tea","ate"],["tan","nat"],["bat"]]

"""


def myFunction(myList):

    myHashmap = {}

    for word in myList:
        key = "".join(sorted(word))

        if key in myHashmap:
            myHashmap[key].append(word) 
        else:
            myHashmap[key] = []
            myHashmap[key].append(word)
    
    result = []
    for key in myHashmap:
        result.append(myHashmap[key])

    return result 





myFunction(["eat","tea","tan","ate","nat","bat"])


# iterate through each item, make a different hashmap for each item AND store the actual string as well
#make an array and add all the hashmaps 
#for each hashmap, if they are similar, they go in one hashmap
# 1 = { {, "string"}, {, "string"}, {, "string"} }
# 2 = ...

# def myFunction(myList):
    
#     items = []
    
#     for x in range(0, len(myList)):
#         # myList[x] = "string"
#         letterHashmap = {}
        
#         for p in myList[x]:
#             if p not in letterHashmap:
#                 letterHashmap[p] = 1
#             else:
#                 letterHashmap[p] = letterHashmap[p] + 1
#         letterHashmap["string"] = myList[x]
#         #items[x] = letterHashmap cannot be done

#         items.append(letterHashmap)

#     #another hashmap: will include all the similar hashmaps
#     BIGHASHMAP = {}

#     # for j in hashmap:
#     print(items)  


# myFunction(["eat","tea","tan","ate","nat","bat"])
#this gets very slow!!!!


# better idea: sort alphabetical of each item and add it as key and let others find you :)
# why is this better? if 




