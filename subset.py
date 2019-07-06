class Solution:
    def subset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        针对没有重复点
        不好，不需要depth和start
        实际上是DFS，不是BFS
        """
        res = []
        def bfs(depth, start, res_list):
            print(res_list)
            # 深度优先搜索
            res.append(res_list)
            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    bfs(depth+1, i+1, res_list+[nums[i]])
        bfs(0, 0, [])
        return res

    def subsets(self, nums):
        if not nums:
            return []
        res = []

        def DFS(depth, tem):
            res.append(tem)
            if depth >= len(nums):
                return
            for i in range(depth, len(nums)):
                DFS(i + 1, tem + [nums[i]])

        DFS(0, [])
        return res


    def subset2(self, nums):
#         有重复点
#          不好，
        nums.sort()
        res = []
        def bfs(depth, start, res_list):
            print(res_list)
            if res_list not in res:
                res.append(res_list)
            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    bfs(depth+1, i+1, res_list+[nums[i]])

        bfs(0,0,[])
        return res



s = Solution()
print(s.subset([1,2,3,4]))
print(s.subset2([1,2,2,4]))