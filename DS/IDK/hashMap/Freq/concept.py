#1. concept: 
''' frequency map is when you have a dictionary counting how often something appears.'''

#2. How the pattern works
'''
1. make a dictionary
2. go through 1 pass of the array and add counter aka value everytime key is seen in array
'''

#3. Use what?
'''
→ Use a HashMap or HashSet.
'''

#4. code template
frequencyDictionary = {}
array = []

for x in array:
    if x not in frequencyDictionary:
        frequencyDictionary[x] = 1
    else:
        frequencyDictionary[x] += 1

# 
