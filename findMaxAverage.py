class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        length = len(nums)
        if length == k:
            return sum(nums)/length

        max_sum = sum(nums[:k])
        first = nums[0]
        for i in range(length - k + 1):
            # print(nums[i:i+k])
            if nums[i+k-1] > first:
                if sum(nums[i:i+k]) > max_sum:
                    max_sum = sum(nums[i:i+k])
            first = nums[i]

        return max_sum / k


    def findMaxAverage2(self, nums, k):
        # 二分法
        length = len(nums)
        if length == k:
            return sum(nums) / length

        i = 0
        j = length - k

        # max_sum = -int("inf")
        while(j >= i):
            if sum(nums[i:i+k]) >= sum(nums[j:j+k]):
                j = j -1
            else:
                i = i + 1
        return sum(nums[i:i+k])/k

    def findMaxAverages3(self, nums, k):
        i, sum_now, max_sum, n, = 0, sum(nums[0:k]), sum(nums[0:k]), len(nums)
        while i < n - k:
            i += 1
            sum_now += (nums[i + k - 1] - nums[i - 1])
            if sum_now > max_sum:
                max_sum = sum_now
        return float(max_sum) / k







s = Solution()
print(s.findMaxAverages3([0,1,1,3,3],k=4))