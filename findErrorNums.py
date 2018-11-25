class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        delta = sum(range(len(nums)+1)) - sum(nums)
        set_num = set(nums)
        mis_num = sum(nums) - sum(set_num)
        return [mis_num, mis_num+delta]



s = Solution()
nums = [1,2,2,4]
print(s.findErrorNums(nums))




