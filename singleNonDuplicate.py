class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)
        return sum(s)*2-sum(nums)

    def singleNonDuplicate2(self, nums):
        r = 0
        for i in nums:
            r ^= i
        return r
#     用位运算的，真是天才！！！！！！








s = Solution()
print(s.singleNonDuplicate2([1,1,2,3,3,4,4,8,8]))