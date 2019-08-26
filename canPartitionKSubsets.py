from typing import List
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def partitionKsubsetCore(nums, index,  each, dp):
            if index < 0:
                return True
            for i in range(len(dp)):
                if (dp[i] + nums[index] == each) or (index > 0 and dp[i] + nums[index] + nums[0]<= each):
                    dp[i] += nums[index]
                    if partitionKsubsetCore(nums, index - 1, each, dp):
                        return True
                    else:
                        dp[i] -= nums[index]
            return False

        if k == 1:
            return True

        if not nums:
            return False
        sums = sum(nums)
        if sums % k != 0:
            return False
        else:
            nums.sort(reverse=False)
            each = sums // k
            if nums[-1] > each:
                return False
            else:
                dp = [0 for _ in range(k)]
                index = len(nums)-1
                return partitionKsubsetCore(nums,index, each, dp)

    def canPartitionKSubsets2(self, nums: List[int], k: int) -> bool:
        if not nums or len(nums) < k:  # 为空或不够分
            return False
        avg, mod = divmod(sum(nums), k)
        if mod:  # 不能整除
            return False
        nums.sort(reverse=True)  # 倒序排列
        if nums[0] > avg:  # 有超过目标的元素
            return False
        used = set()  # 记录已使用的数

        # 凑数时永远考虑将数从大到小排列来凑数，这样可以避免重复的情况
        def dfs(k, start=0, tmpSum=0):  # 当前还需要凑的avg个数，当前从哪个数开始考虑，以及当前已凑够的和
            if tmpSum == avg:  # 如果已凑满一个
                return dfs(k - 1, 0, 0)  # 那么从最大数重新开始考虑，凑下一个
            if k == 1:  # 只剩最后一个，那么剩下的没使用的数加起来肯定凑满
                return True
            for i in range(start, len(nums)):  # 优先用大的数的凑
                if i not in used and nums[i] + tmpSum <= avg:  # 如果该数未使用并且可以用来凑
                    used.add(i)  # 使用该数
                    if dfs(k, i + 1, nums[i] + tmpSum):  # 继续用比该数小的数来凑
                        return True
                    used.remove(i)  # 没有得到可用方案，则换个数来凑
            return False

        return dfs(k)


s = Solution()
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(s.canPartitionKSubsets(nums, k))

nums = [2,2,2,2,3,4,5]
k = 4
print(s.canPartitionKSubsets(nums, k))
