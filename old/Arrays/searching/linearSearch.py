num = []
target = 5
#does the number exist? linear search!!!!
#search through the entire list!!!
#O(n) worst case and best case = 0(1)


if len(num) < 1:
    print("FALSE!!")
for x in range(0, len(num)):
    if num[x] == target:
        print("TRUE!!")