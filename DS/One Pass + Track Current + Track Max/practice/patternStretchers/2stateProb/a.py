list = [2,4,6,1,8,10] #→ 3

counter = 0
best = 0

for x in range(0, len(list)):
    if len[x] // 2 == 0:
        counter = counter + 1
    else:
        counter = 0
    
    if counter > best:
        best = counter


