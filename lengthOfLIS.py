# https://blog.csdn.net/u012505432/article/details/52228945


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = 0
        dp = [0 for _ in range(len(nums))]
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i+j) // 2
                if dp[m] < x:
                    i = m + 1
                else:
                    j = m
            dp[i] = x
            size = max(i+1, size)
        #     用二分查找到比x大的最小的那个数更新之
        # 如果需要求的是非严格单调递增数组，只需要把if tails[m] < x:改为if tails[m] <= x:即可
        return size




nums = [10,9,2,5,3,7,101,18]

s = Solution()
print(s.lengthOfLIS(nums=nums))