class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums)== 1:
            return 0

        total = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left == (total - nums[i])/2:
                return i
            else:
                left += nums[i]
        return -1





nums = [1, 2,3]
s = Solution()
print(s.pivotIndex(nums))