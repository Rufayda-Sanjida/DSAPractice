'''
Goal: Move all 0s to the end while keeping the order.
logic is: So basically theres two pointers where one is keeping track of the END of the new list of non zeros (so this pointer holds on to the first 0) and another pointer that simply goes through the entire list only stopping when non zeros are found and then a swap happens and the first pointer is incremented so that it doesnt sit on the newly swapped non zero but the next 0
Why is this problem Two pointers? This is a 2 pointers second type of problem where slow and fast pointers move independently. one keeping track of 0s and the other one looking out for none 0s
'''

def moveZeroes(nums):
    slow = 0 #beginning index
    for fast in range(0, len(nums)): #fast just goes on finding none zero numbers and swapping them with slow who is holding on to first 0
        if nums[fast] != 0:
            storage = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = nums[slow]
            
            slow += 1 #we increment the slow so that it sits at the next 0 not the new non zero that we got swapped with 

list = [1, 2, 0, 3, 0, 4]
moveZeroes(list)
print(list)