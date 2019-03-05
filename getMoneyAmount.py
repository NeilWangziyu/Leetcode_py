class Solution:
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        dp[i][j]表示从[i,j]中猜出正确数字所需要的最少花费金额.(dp[i][i] = 0)
        假设在范围[i,j]中选择x, 则选择x的最少花费金额为: max(dp[i][x-1], dp[x+1][j]) + x
        """
        DP = [[0 for _ in range(n + 2)] for _ in range(n + 2)]

        for i in range(n, 0, -1):
            for j in range(i, n + 1, 1):
                if i == j:
                    DP[i][j] = 0
                else:
                    DP[i][j] = float('inf')
                    for index in range(i, j + 1, 1):
                        DP[i][j] = min(DP[i][j], max(DP[i][index - 1], DP[index + 1][j]) + index)
        print(DP)
        return DP[1][n]

    def getMoneyAmount2(self, n):
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for l in range(n - 1, 0, -1):
            for r in range(l + 1, n + 1):
                dp[l][r] = min(i + max(dp[l][i - 1], dp[i + 1][r]) for i in range(l, r))
        return dp[1][n]


if __name__ == "__main__":
    s = Solution()
    print(s.getMoneyAmount(10))