class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum_num = sum(nums)

        average = sum_num // len(nums)

        delta = abs( sum_num - average * len(nums))

        res = 0
        for each in nums:
            res += abs(each - average)

        return res + delta



s = Solution()
print(s.minMoves2([1,2,3]))