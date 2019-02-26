class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        dp[n]:最大值为nums[n]的满足题意的子集元素个数
        """
        if not nums:
            return []
        length = len(nums)
        nums.sort()
        dp = [1] * length
        pre = [-1] * length
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        pre[i] = j
        print(dp)
        print(pre)
        max_index = dp.index(max(dp))
        res = []
        while (max_index != -1):
            res.append(nums[max_index])
            max_index = pre[max_index]
        return res


nums = [1,2,3,4,5,6,7,8,9,10]
s = Solution()
print(s.largestDivisibleSubset(nums))