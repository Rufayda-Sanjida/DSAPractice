# 45. Jump Game II

'''
I believe same concept as before:

- each index represents how far or less you can jump from that position
- each element you can go over or less: element 4 : 4 or less jumps
- your jumps cannot go above n (n-1 is last index)

- minimum number of jumps
'''




def jumpGame(nums):
    jumps = 0
    furthestJumpAvailable = 0
    jump_end = 0

    for x in range(0, len(nums)-1):

        # if x > furthestJumpAvailable:
        #     break # not possible!!!
    
        # if we are already at the last index

        # we reached the end:
        if (nums[x] + x) >= len(nums) - 1:
            # if we CAN reach then we make the jump!
            jumps += 1
            break;

        # we need to update the furthest we can go!
        if (nums[x] + x) > furthestJumpAvailable:
            furthestJumpAvailable = nums[x] + x
        
        # did we use up a jump?
        if x == jump_end:
            jumps = jumps + 1
            jump_end = furthestJumpAvailable

    return jumps


nums = [0]
print(jumpGame(nums))
