class Solution:
    def subset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def dfs(depth, start, res_list):
            print(res_list)
            # 广度优先搜索
            res.append(res_list)
            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    dfs(depth+1, i+1, res_list+[nums[i]])


        dfs(0, 0, [])
        return res

s = Solution()
print(s.subset([1,2,3,4]))