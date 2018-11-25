class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # print(sum(nums))
        return (3*sum(set(nums)) - sum(nums))//2




# 最优解法：使用位运算 res ^= x, res ^= x ,之后res还原，令res等于零，最后得到的就是那个唯一的值

s = Solution()
print(s.singleNumber([2,2,3,2]))