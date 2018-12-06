class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if sum(nums) == S or sum(nums) == -S:
            t = len([i for i in nums if i == 0])
            return 2 ** t

        t1 = self.findTargetSumWays(nums[1:], S - nums[0])
        t2 = self.findTargetSumWays(nums[1:], S + nums[0])
        # print(t1, t2)
        return t1 + t2


    def findTargetSumWays2(self, nums, S):

        def DFS(index, length, target):
            if index == length-1:
                if target == nums[index] or target == - nums[index]:
                    if target == 0:
                        return 2
                    else:
                        return 1
                else:
                    return 0
            else:
                return DFS(index+1, length, target-nums[index])+DFS(index+1, length, target+nums[index])

        if len(nums) == 0:
            return 0
        return DFS(0, len(nums), S)


    def findTargetSumWays3(self, nums, S):

        if sum(nums) < S:
            return 0

        if (S + sum(nums)) % 2 == 1:
            return 0

        target = (S+sum(nums))//2
        print(target)
        # target is sum(positive)

        dp_list = [0 for _ in range(target+1)]
        print(dp_list)
        dp_list[0] = 1
        for each in nums:
            for i in range(target, each-1, -1):
                dp_list[i] = dp_list[i] + dp_list[i-each]
        return dp_list[target]








# nums = [10,9,6,4,19,0,41,30,27,15,14,39,33,7,34,17,24,46,2,46]
# S = 45
nums = [1000]
S = -1000
# nums = [25,33,27,23,46,16,10,27,33,2,12,2,29,44,49,40,32,46,7,50]
# S = 4
s = Solution()
print(s.findTargetSumWays3(nums, S))

