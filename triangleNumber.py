def triangleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # count = 0
    # if len(nums) < 3:
    #     return 0
    # nums.sort()
    # for i in range(len(nums)):
    #     for j in range(i + 1, len(nums)):
    #         min_len = nums[j] - nums[i]
    #         max_len = nums[j] + nums[i]
    #         result = len([t for t in nums[j+1:] if t>min_len and t<max_len])
    #         count += result
    # return count

    cnt = 0
    nums.sort(reverse=True)
    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > nums[i]:
                cnt += right - left
                left += 1
            else:
                right -= 1
    return cnt




nums = [55,51,54,9,84,16,13,69,53,10,82,36,7,60,65,33,25,73,45,18,72,73,26,25,61,54,2,35,31,90,41,88,63,69,13,36,50,84,97,47,94,75,92,88,6,25,29,8,23,76,47,60,86,56,60,45,76,74,67,37,35,24,11,35,28,81,65,78,31,51,48,100,42,73,47,57,62,60,48,75,100,0,11,55,77,40,74,57,45,77,72,43,48,40,9,94,62,30,62,34]
print(triangleNumber(nums))