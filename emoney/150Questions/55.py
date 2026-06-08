
# jump game
# each position represents how far you can jump from that position or less
# return true if we can jump to the last index


'''
solution; we just figure out if we CAN get to the end,
at every index, calculate furthest you can go AND if it reaches the end
# at every index, figure out with the furthest IF we can even be in the current index
'''

nums = [1]

furthest = 0

answer = False

for x in range(0, len(nums)):
    
    # Can we even be at the current index?
    if x > furthest:
        break
    else: 
        currentFarthest = nums[x] + x
       
        # is the furthest reaching end?
        if currentFarthest >= len(nums)-1:
            answer = True
            break

        # is the furthest this index goes is the farthest we can go period?
        elif currentFarthest > furthest:
            furthest = currentFarthest


print(answer)  


# def canJump(nums):

#     furthest = 0

#     for x in range(0, len(nums)):
        
#         # Can we even be at the current index?
#         if x > furthest:
#             break
#         else: 
#             currentFarthest = nums[x] + x
        
#             # is the furthest reaching end?
#             if currentFarthest == len(nums)-1:
#                 return True

#             # is the furthest this index goes is the farthest we can go period?
#             elif currentFarthest > furthest:
#                 furthest = currentFarthest

#     return False