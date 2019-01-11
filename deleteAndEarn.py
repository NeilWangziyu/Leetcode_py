class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import collections

        if len(nums) == 1:
            return nums[0]


        total_num = list(set(nums))

        max_num = max(total_num)

        check_list = [0 for _ in range(max_num+1)]
        nums_list = [0 for _ in range(max_num+1)]

        for each in nums:
            nums_list[each] += each

        check_list[1] = nums_list[1]
        check_list[2] = max(nums_list[1], nums_list[2])

        for i in range(3, max_num+1):
            check_list[i] = max(nums_list[i] + check_list[i-2], check_list[i-1])



        return check_list[-1]





nums = [2, 2, 3, 3, 3, 4]
s = Solution()
print(s.deleteAndEarn(nums))