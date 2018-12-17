class Solution:
    def subset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        针对没有重复点
        """
        res = []
        def bfs(depth, start, res_list):
            print(res_list)
            # 广度优先搜索
            res.append(res_list)
            if depth == len(nums):
                return
            else:
                for i in range(start, len(nums)):
                    bfs(depth+1, i+1, res_list+[nums[i]])


        bfs(0, 0, [])
        return res

    def subset2(self, nums):
#         有重复点
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