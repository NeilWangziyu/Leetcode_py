class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 2:
            return min(nums)

        res = 0
        nums.sort()
        for i in range(0, length, 2):
            res += nums[i]
        return res


    def arrayPairSum2(self, nums):

        nums.sort()
        return sum(nums[::2])


s = Solution()
print(s.arrayPairSum([1,4,3,2]))
