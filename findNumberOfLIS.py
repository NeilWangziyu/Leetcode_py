class Solution:
    max_length = 0
    count = 0
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        超时了可惜
        理应用动态规划的方法求解
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        res = []
        def bfs(depth, start, res_list):
            res.append(res_list)
            if len(res_list) > self.max_length:
                self.max_length = len(res_list)
                self.count = 1
            elif len(res_list) == self.max_length:
                self.count += 1

            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    if res_list == [] or nums[i]> res_list[-1]:
                        bfs(depth+1, i+1, res_list+[nums[i]])
                    # else:
                    #     if nums[i]> res_list[-1]:
                    #         bfs(depth + 1, i + 1, res_list + [nums[i]])
        bfs(0, 0, [])

        return self.count


    def findNumberOfLIS2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        利用动态规划
        用dp[i]表示以nums[i]为结尾的递推序列的长度，
        用cnt[i]表示以nums[i]为结尾的递推序列的个数，
        初始化都赋值为1，只要有数字，那么至少都是1。
        然后我们遍历数组，对于每个遍历到的数字nums[i]，
        我们再遍历其之前的所有数字nums[j]，当nums[i]小于等于nums[j]时，
        不做任何处理，因为不是递增序列。反之，则判断dp[i]和dp[j]的关系，
        如果dp[i]等于dp[j] + 1，说明nums[i]这个数字可以加在以nums[j]结尾的递增序列后面，
        并且以nums[j]结尾的递增序列个数可以直接加到以nums[i]结尾的递增序列个数上。
        如果dp[i]小于dp[j] + 1，说明我们找到了一条长度更长的递增序列，
        那么我们此时奖dp[i]更新为dp[j]+1，并且原本的递增序列都不能用了，
        直接用cnt[j]来代替。维护一个全局最长的子序列长度mx，每次都进行更新，
        到最后遍历一遍每个节点，如果长度等于mx,res+=cnt[i];
        """
        if not nums:
            return 0
        dp = [1 for _ in range(len(nums))]
        cnt = [1 for _ in range(len(nums))]
        max_len = 1
        for i, num in enumerate(nums):
            for j, p_num in enumerate(nums[:i]):
                if nums[i] <= nums[j]:
                    continue
                else:
                    if dp[i] == dp[j]+1:
                        cnt[i] += cnt[j]

                    elif dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
            max_len = max(max_len, dp[i])

        print(dp)
        print(cnt)
        res = 0

        for i in range(len(nums)):
            if dp[i] == max_len:
                res += cnt[i]
        return res


    def findNumberOfLIS3(self, nums) -> int:
        '''
        https://leetcode.com/articles/number-of-longest-increasing-subsequence/
        '''
        N = len(nums)
        if N <= 1:
            return N
        lengths = [0] * N  # lengths[i] = longest ending in nums[i]
        counts = [1] * N  # count[i] = number of longest ending in nums[i]

        for j in range(N):
            for i in range(j):
                if nums[i] < nums[j]:
                    if lengths[i] >= lengths[j]:
                        lengths[j] = 1 + lengths[i]
                        counts[j] = counts[i]
                    elif lengths[i] + 1 == lengths[j]:
                        counts[j] += counts[i]

        maxlen = max(lengths)
        return sum(counts[i] for i in range(N) if lengths[i] == maxlen)


s = Solution()


nums = [1,3,5,4,7]
print(s.findNumberOfLIS2(nums))
nums = [3,1,2]
print(s.findNumberOfLIS2(nums))

nums = [1,2,4,3]
print(s.findNumberOfLIS2(nums))

nums= [2,2,2,2,2]
print(s.findNumberOfLIS2(nums))

nums = [0,7,1,3,6,0,0,4,9,10]
print(s.findNumberOfLIS2(nums))

nums = [0,7,1,3,6,0,0,4,9,10,5,7,2,10,3,3,0,5,7,2,3,5,8,-9,10,6,7,1,1,2,9,0,1,5,10,8,1,9,6,7,5,8,4,-1,6,5,7,0,3,4,8,9,9,3,7,9,1,3,10,7,9,5,10,1,2,9,9,7,3,5,2,0,3,1,8,7,9,2,6,4,1,6,5]
print(s.findNumberOfLIS2(nums))
