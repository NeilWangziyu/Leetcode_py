def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    jump_max = 0
    for i in range(len(nums)-1):
        if (i <= jump_max) and (i + nums[i] > jump_max):
            jump_max = i + nums[i]

        print(jump_max)

    if jump_max >= len(nums)-1:
        return True
    else:
        return False


# print(canJump([2,3,1,1,4]))
# print(canJump([3,2,1,0,4]))
print(canJump([0, 2, 3]))
