class Solution:
    def sortArray(self, nums):
        if not nums:
            return nums
        if len(nums) == 1:
            return nums
        inv = nums[0]
        left = []
        right = []
        for each in nums[1:]:
            if each > inv:
                right.append(each)
            else:
                left.append(each)
        return self.sortArray(left) + [inv] + self.sortArray(right)
