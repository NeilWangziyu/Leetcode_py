class Solution:
    flag = False
    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        # 涂色思路
        # https://leetcode-cn.com/articles/possible-bipartition/
        """
        import collections
        graph = collections.defaultdict(list)
        print(graph)
        for u, v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        color = {}

        def dfs(node, c=0):
            if node in color:
                return color[node] == c
            color[node] = c
            return all(dfs(nei, c ^ 1) for nei in graph[node])

        return all(dfs(node)
                   for node in range(1, N + 1)
                   if node not in color)




    def dfs(self, colors, index, dp, color):
        print(colors, index, dp, color)
        if colors[index] != -1:
            return color == colors[index]
        colors[index] = color
        for x in dp[index]:
            if not self.dfs(colors, x, dp, 1 - color): return False
        return True
    def possibleBipartition2(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        二分图 用颜色标志每个点  加颜色过程中如果出现冲突则表明 不能形成二分图 也就不能二分
        """

        dp = [[] for _ in range(N + 1)]
        colors = [-1] * (N + 1)
        colors[0] = 1

        for x, y in dislikes:
            dp[x].append(y)
            dp[y].append(x)
        # dp[i]:和i点不能一起出现的点
        print(dp)
        print(colors)
        for i in range(1, N + 1):
            if colors[i] == -1 and not self.dfs(colors, i, dp, 1): return False
        return True






N = 3
dislikes = [[1,2],[1,3],[2,3]]

s = Solution()
print(s.possibleBipartition2(N, dislikes))