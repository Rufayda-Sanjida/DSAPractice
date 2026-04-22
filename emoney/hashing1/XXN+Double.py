#Goal: Return True if array contains

inputList = [10,2,5,3]

def nAndDouble(input):
    mySet = set()

    for x in input:
        if x not in mySet:
            double = x * 2
            if double in mySet:
                return True
            
            mySet.add(x)
        
    return False

print(nAndDouble(inputList))
