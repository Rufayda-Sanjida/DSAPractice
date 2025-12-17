#3. LC 2027 – Minimum Moves to Convert String (variant of streak)

s = "XXOX" 
# s = "XXOXXX" 
count = 0

i = 0
while i < len(s)-2:
    if s[i] == "X":
        i = i + 3
        count = count + 1


if i < len(s):
    #may be extra x
    if i + 1 == len(s) and s[i] == "X":
        count +=1
    elif i + 2 == len(s) and s[i+1] == "X":
        count +=1
    
print(count)