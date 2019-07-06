class Solution:
    """
    所有的子集和排列
    """
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def bfs(depth, start, value_list):
            res.append(value_list)
            if depth == len(nums):
                return
            for i in range(start, len(nums)):
                bfs(depth+1, i+1, value_list+[nums[i]])

        res = []
        bfs(0, 0, [])
        return res


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        print ('nums', nums)
        if len(nums) <= 1:
            return [nums]
        ans = []
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1:]
            # n:没有某一个数，剩余的全排列
            for temp_list in self.permute(n):
                # temp_list：剩余的排列结果
                ans.append([num] + temp_list)
            print ('-----End-----')
        return ans

s = Solution()
print(s.subsets([12,4,5,6]))
print('\n')
print(s.permute([12,4,5,6]))

