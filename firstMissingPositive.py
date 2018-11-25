def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    def busket_sort(nums):
        for i in range(len(nums)):
            print("i",i)
            while (nums[i] != i + 1):
                print(nums[i])
                if nums[i] > len(nums) or nums[i] < 1 or nums[nums[i] - 1] == nums[i]:
                    break
                else:
                    num_to_change = nums[nums[i] - 1]
                    index_to_change = nums[i] - 1
                    nums[index_to_change] = nums[i]
                    nums[i] = num_to_change

        return nums

    nums = busket_sort(nums)
    print(nums)
    length = len(nums)
    for i in range(length):
        if nums[i] != i + 1:
            return i + 1
    return i + 2


print(firstMissingPositive([3,4,-1,1]))