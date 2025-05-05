arr = [3,1,7,11]

#arr[i] == 2 * arr[j] does this relationship exist?
breakCode = False

for x in range(0, len(arr)):
    if x == len(arr)-1:
        print("You done got to the end of the list and didnt find this relationship. it happens sorry")
    for j in range(x + 1, len(arr)):
        if arr[x] == 2 * arr[j]:
            print("YESS GODDD")
            breakCode = True
            break
    if breakCode == True:
        break

