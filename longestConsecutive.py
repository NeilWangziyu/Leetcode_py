class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums = list(set(nums))
        if len(nums) == 1:
            return 1
        max_res = 1
        res = 1

        nums.sort()
        print(nums)
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                res += 1
            else:
                if res > max_res:
                    max_res = res
                res = 1

        if res > max_res:
            max_res = res

        return max_res




nums = [1,2,0,1]
s = Solution()
print(s.longestConsecutive(nums))