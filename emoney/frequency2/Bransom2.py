#Goal:
# Return True if you can construct the ransom note from magazine letters

# ransome note is a bunch of letters and magazine is too
#  magazine letters is whole, can number of letters and letters themselves be in the magazine letters?
# we are dealing with storing the frequency of items in a list - magazine that is!


def myFunction(ransomNote, magazine):

    frequencyOfMagazineLetters = {}

    for x in magazine:
        if x not in frequencyOfMagazineLetters:
            frequencyOfMagazineLetters[x] = 1
        else:
            frequencyOfMagazineLetters[x] = frequencyOfMagazineLetters[x] + 1

    # print(frequencyOfMagazineLetters)


    for i in ransomNote:
        if i in frequencyOfMagazineLetters:
            if frequencyOfMagazineLetters[i] == 0:
                return ("Ransome CANNOT be made from magazine")
            
            frequencyOfMagazineLetters[i] = frequencyOfMagazineLetters[i] - 1
        else:
            return ("Ransome CANNOT be made from magazine")
    
    return ("Ransome CAN be made from magazine")


ransomNote = "aa"
magazine = "aab"

print(myFunction(ransomNote, magazine ))
#Output: True