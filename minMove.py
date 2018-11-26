class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = min(nums)
        res = 0
        for each in nums:
            res += each - n
        return res


s = Solution()
print(s.minMoves([1,2,3]))