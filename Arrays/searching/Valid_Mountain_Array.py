arr = [0,2,3,4,5, 2, 1, 0]

def mountain(arr):
    if len(arr) < 3:
        #print("NOT A DAMN Mountain")
        return ("NOT A DAMN Mountain")
    
    #must consistantly go up and then must consistantly go down!

    strictlyInc = 1
    strictlyDec = 0

    for x in range(1, len(arr)):
        
        if arr[x-1] < arr[x] and strictlyInc == 1:
            continue
        elif arr[x-1] > arr[x] and strictlyDec == 1:
            continue
        elif arr[x-1] > arr[x] and strictlyInc == 1:
            strictlyInc = 0
            strictlyDec = 1
        else:
            #print("not a mountain")
            return("not a mountain")
    
    return ("is a mountain")
    
print(mountain(arr))    