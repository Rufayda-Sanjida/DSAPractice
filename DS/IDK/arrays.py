list = [1, 2, 3, 4, 5]

#access (index): 0(1)
print(list[0])

# Update: O(1)
list[0] = "hello"
print(list)

#Insert/delete at end: 
# O(1) over time since you need to increase ( O(n) ) here and there
list = [1, 2, 3, 4, 5]
list.append(5)
print(list)
list.pop(5)
print(list)

#Insert/delete in the front or middle:  O(n)
list = [1, 2, 3, 4, 5]
list.append(5)
