class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return None
        if len(nums) ==4:
            if sum(nums) == target:
                return [nums]
            else:
                return None
        nums.sort()
#         固定前两个，然后检查后面的



nums = [1, 0, -1, 0, -2, 2]
target = 0

s = Solution()
print(s.fourSum(nums, target))
