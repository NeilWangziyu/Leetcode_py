class Solution:
    def canPartition(self, nums) -> bool:
        # 判断哪些值能够取到，必须要取到sum//2
        if not nums:
            return False
        if len(nums) <= 1:
            return False

        sums = sum(nums)
        if sums % 2 != 0:
            return False

        dp = [False for _ in range(sums+ 1)]
        dp[0] = True
        for each in nums:
            for i in range(sums, -1, -1):
                if dp[i]:
                    dp[i+each] = True

            if dp[sums // 2]:
                return True
        return False

    def canPartition2(self, nums) -> bool:
        nums = sorted(nums, reverse=True)
        num = sum(nums)

        if num % 2 == 1:
            return False

        num = num / 2
        if max(nums) > num:
            return False

        n = len(nums)

        def dg(nums, ind, num):
            if num == 0:
                return True
            if num < 0 or len(nums) == 0:
                return False
            for i in range(ind, n):
                if dg(nums, i + 1, num - nums[i]):
                    return True
            return False

        return dg(nums, 0, num)


s = Solution()
print(s.canPartition(nums=[1, 5, 11, 5]))
