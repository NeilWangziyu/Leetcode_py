class Solution:
    def jump(self, nums) -> int:
        """
        超时
        :param nums:
        :return:
        """
        if len(nums) == 1:
            return 0
        dp = [float('inf') for _ in range(len(nums))]
        dp[0] = 0
        for i in range(len(nums)-1):
            for index in range(i+1, min(i + nums[i] + 1, len(nums))):
                dp[index] = min(dp[index], dp[i]+1)
        return int(dp[-1])

    def jump2(self, nums) -> int:
        if len(nums) == 1:
            return 0
        step = 0
        i = 0
        left = 0
        right = 0
        while (right < len(nums) - 1):
            m = 0
            while(i <= right):
                m = max(i + nums[i], m)
                i += 1
            left = right + 1
            right = m
            step += 1
        return step

    def jump3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        if len(set(nums)) == 1:
            return (len(nums) - 2) // nums[0] + 1
        pos = [len(nums) - 1]
        temp = len(nums) - 1
        count = 0
        while 0 not in pos:
            count += 1
            for j in range(temp):
                if nums[j] + j >= temp:
                    temp = j
                    pos.append(j)
                    break
        return count


s = Solution()
print(s.jump(nums=[2,3,1,1,4]))
print(s.jump2(nums=[2,3,1,1,4]))