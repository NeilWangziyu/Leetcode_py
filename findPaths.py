class Solution(object):
    res = 0
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        def DFS(m, n, N, i, j, count):
            if count > N:
                return
            if i < 0 or j < 0 or i >= m or j >= n:
                self.res += 1
            else:
                DFS(m, n, N, i-1, j, count+1)
                DFS(m, n, N, i + 1, j, count + 1)
                DFS(m, n, N, i, j-1, count + 1)
                DFS(m, n, N, i, j+1, count + 1)
                return

        DFS(m, n, N, i, j, 0)
        return self.res % (10**9+7)

    def findPaths2(self, m, n, N, i, j):
        """
        使用三位数组 dp[i][j][k] 表示从(i, j)开始在k步内移除边界的路径数。对于每个[i, j, k]尝试
        上下左右四个方向进行移动。

        如果下一步出界，则dp[row][col][k] += 1;
        否则 dp[row][col][k] = (dp[row][col][k] + dp[nextRow][nextCol][k-1]) % mod;
        //从[row, col]移动到[nextRow, nextCol]需要花费一步
        """
        if m == 0 or n == 0 or N == 0:
            return 0

        # 优化：可以不需要k
        mod = 1000000007

        dp = [[0 for _ in range(n)] for _ in range(m)]
        dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        for k in range(N):
            tem = [[0 for _ in range(n)] for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    for dir in dirs:
                        nx = x + dir[0]
                        ny = y + dir[1]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            tem[x][y] += 1
                        else:
                            tem[x][y] = (dp[nx][ny] + tem[x][y]) % mod
            dp = tem
        return dp[i][j]

    def findPaths3(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        BIG = 10 ** 9 + 7
        board = [[0] * n for _ in range(m)]
        board[i][j] = 1
        ans = 0
        moves = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for k in range(N):
            temp = [[0] * n for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    if board[r][c] != 0:
                        for move in moves:
                            nxtr = r + move[0]
                            nxtc = c + move[1]
                            if 0 <= nxtr < m and 0 <= nxtc < n:
                                temp[nxtr][nxtc] += board[r][c]
                            else:
                                ans += board[r][c]
                                ans %= BIG
            for r in range(m):
                board[r] = temp[r][:]
        return ans


m = 5
n = 5
N = 30
i = 0
j = 0
s = Solution()
# print(s.findPaths(m, n, N, i, j))
print(s.findPaths2(m, n, N, i, j))