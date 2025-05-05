a = "11"
b = "1"

top = len(a)-1
bottom = len(b)-1
carry = 0
result = []

while (top >= 0) or (bottom >= 0):
    if a[top] == "0" and b[bottom] == "0" and carry == 0:
        result.append("0")
    
    if a[top]== "1" and b[bottom]  == "0" and carry == 0:
        result.append("1")    
    
    if a[top] == "0" and b[bottom]  == "1" and carry == 0:
        result.append("1")  
    
    if a[top] == "0" and b[bottom]  == "0" and carry == 1:
        result.append("1")
        carry = 0
    
    if a[top] == "1" and b[bottom]  == "1" and carry == 1:
        result.append("1")
        carry = 1
    
    
    
    if a[top] == "1" and b[bottom]  == "1" and carry == 0:
        result.append("0")
        carry = 1
    
    if a[top] == "1" and b[bottom]  == "0" and carry == 1:
        result.append("0")
        carry = 1
        
    if a[top] == "0" and b[bottom]  == "1" and carry == 1:
        result.append("0")
        carry = 1
    
    top = top - 1 
    bottom = bottom - 1
    
      

#append the rest to the list AFTER checking result



newFlippedList = []

for x in range(len(result)-1, -1, -1):
    newFlippedList.append(result[x])
    

string = "".join(newFlippedList)
print(string)



