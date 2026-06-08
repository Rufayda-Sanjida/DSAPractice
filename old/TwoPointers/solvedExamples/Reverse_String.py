'''
Goal: you are given SORTED array and you must reverse the array 
logic is: use two pointers one at the front and the other one at the end and each round, swap their values and move closer and closer switching each round
Why is this problem Two pointers? I am keeping tracking of 2 pointers coming closer to each other but never surpassing and each round I just swap
'''

list = [1, 2, 3, 4, 5]

front = 0
end = len(list)-1

while front < end:
    hold = list[end]
    list[end] = list[front]
    list[front] = hold
    front = front + 1
    end = end - 1

print(list)