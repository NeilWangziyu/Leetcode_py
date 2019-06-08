class Solution:
    # 连续
    res = 0
    def numSubarrayProductLessThanK(self, nums, k) -> int:
        """
        超时
        """
        def subarrayLessThanK(depth, tem_res, k, tem_list):
            if depth >= len(nums) or tem_res >= k:
                return
            if tem_res * nums[depth] < k:
                # print(tem_list+[nums[depth]])
                self.res += 1
            subarrayLessThanK(depth+1, tem_res*nums[depth], k, tem_list + [nums[depth]])

        if not nums:
            return 0

        self.res = 0
        for i in range(len(nums)):
            subarrayLessThanK(i, 1, k, [])

        return self.res

    def numSubarrayProductLessThanK2(self, nums, k: int) -> int:
        if (k == 0 or k == 1):
            return 0
        l = 0
        sum_tem = 0
        res = 1
        for r in range(len(nums)):
            res *= nums[r]
            while (res >= k):
                res /= nums[l]
                l += 1
            sum_tem += (r - l + 1)
        return sum_tem

    def numSubarrayProductLessThanK3(self, nums, k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans






nums = [10, 5, 2, 6]
k = 100
s = Solution()
print(s.numSubarrayProductLessThanK(nums, k))
print(s.numSubarrayProductLessThanK2(nums, k))