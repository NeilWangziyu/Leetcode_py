class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # 实际上更为简便的方法是通过一个矩阵对其进行计算
        if not obstacleGrid:
            return 0

        # if len(obstacleGrid) == 1 and len(obstacleGrid[0]) == 1:
        #     if obstacleGrid[0][0] == 1:
        #         return 0
        #     else:
        #         return 1
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0]:
            return 0

        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        new_list = [[0 for i in range(m)] for j in range(n)]
        # print(new_list)
        new_list[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[0][i] == 1:
                new_list[0][i] = 0
            else:
                new_list[0][i] = new_list[0][i - 1]

        for j in range(1, n):
            if obstacleGrid[j][0] == 1:
                new_list[j][0] = 0
            else:
                new_list[j][0] = new_list[j - 1][0]

        # print(new_list)
        for row in range(1, n):
            for col in range(1, m):
                print(row, col, obstacleGrid[row][col])
                if obstacleGrid[row][col] == 0:
                    new_list[row][col] = new_list[row - 1][col] + new_list[row][col - 1]
                else:
                    new_list[row][col] = 0
        # print(new_list)

        return new_list[n - 1][m - 1]




x = [[0,0],[1,1],[0,0]]

S = Solution()
print(S.uniquePathsWithObstacles(x))