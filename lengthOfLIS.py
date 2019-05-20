# https://blog.csdn.net/u012505432/article/details/52228945


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        dp是一个数组，用于存储在dp[i]中，所有长度为i+1的递增子序列的最小的尾元素
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
            print(dp)
        #     用二分查找到比x大的最小的那个数更新之
        # 如果需要求的是非严格单调递增数组，只需要把if dp[m] < x:改为if dp[m] <= x:即可
        print(dp)
        return size

    def lengthOfLIS2(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        print(dp)
        return max(dp)




nums = [100,101,102,103,104,10,9,2,5,3,7,101,18]

s = Solution()
print(s.lengthOfLIS(nums=nums))
print(s.lengthOfLIS2(nums=nums))