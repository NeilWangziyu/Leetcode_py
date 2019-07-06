class Solution:
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        tip = len(nums) // 2
        res = 0
        for each in nums:
            res += abs(each - nums[tip])
        return res




nums = [203125577,-349566234,230332704,48321315,66379082,386516853,50986744,-250908656,-425653504,-212123143]

# nums = [1, 0, 0, 8, 6]
s = Solution()
print(s.minMoves2(nums))



