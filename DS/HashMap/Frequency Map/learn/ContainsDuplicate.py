#Question: Do any numbers appear more than once?

'''
Thought process (IMPORTANT)

I don't care where

I don't care how many

I just care if count ≥ 2

Pattern recognition

✔ “duplicate”
✔ “appear more than once”
→ Frequency Map

'''


array = [1, 2, 3, 4, 1, 3, 4, 6, 8]
hashmap = {}

for x in array:
    # store it
    if x not in hashmap: #IMPORTANT: hashmap[x] does not exist so you check is the key is even in the hashmap
        hashmap[x] = 1
    else:
        hashmap[x] = hashmap[x] + 1
    
    if hashmap[x] > 1:
        print(f"we have a duplicate! and thats {x}")
        break
