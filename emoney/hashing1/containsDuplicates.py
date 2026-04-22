Input = [1,2,3,1]
#Output: True

def containsDuplicates2(Input):
    mySet = set()

    for x in Input:
        if x not in mySet:
            mySet.add(x)
        else:
            return True

    return False 


print(containsDuplicates2(Input))

